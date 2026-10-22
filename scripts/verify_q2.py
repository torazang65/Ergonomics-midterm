"""Q2 계산 및 검산.

정의는 work/q2/definitions.md 를 따른다. 표준 라이브러리만 사용한다.
실행: python3 scripts/verify_q2.py [input.json]  (기본 work/q2/input.json)
"""
import json
import math
import sys
from pathlib import Path
from statistics import NormalDist

ROOT = Path(__file__).resolve().parent.parent
N01 = NormalDist()
EPS = 1e-12
failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)
    return cond


def plog(p):
    # 0·log2(0) = 0
    return 0.0 if p == 0 else -p * math.log2(p)


def entropy(probs):
    return sum(plog(p) for p in probs)


def sdt(d):
    s_n, h, n_n, fa = d["signal_n"], d["hit"], d["noise_n"], d["false_alarm"]
    check(0 <= h <= s_n and 0 <= fa <= n_n, "SDT 빈도 범위")
    ph, pfa = h / s_n, fa / n_n
    check(0 < ph < 1 and 0 < pfa < 1, "P(H), P(FA)가 0 또는 1이면 z 변환 불가")
    z_h, z_fa = N01.inv_cdf(ph), N01.inv_cdf(pfa)
    d_prime = z_h - z_fa
    beta = N01.pdf(z_h) / N01.pdf(z_fa)
    c = -(z_h + z_fa) / 2
    # 검산: 등분산 모형에서 ln β = d'·c
    check(abs(math.log(beta) - d_prime * c) < 1e-9, "ln β = d'·c 불일치")
    # 검산: 기준점 xc 에서 직접 밀도비 (N~N(0,1), SN~N(d',1))
    xc = -z_fa
    beta_direct = NormalDist(d_prime, 1).pdf(xc) / N01.pdf(xc)
    check(abs(beta - beta_direct) < 1e-9, "β 밀도비 직접 계산 불일치")
    check(abs(NormalDist(d_prime, 1).cdf(xc) - (1 - ph)) < 1e-9, "기준점에서 P(M) 재현 실패")
    # 강의 p.36-38 방식: z 를 표에서 소수 둘째 자리로 읽은 경우
    zt_h, zt_fa = round(z_h, 2), round(z_fa, 2)
    return {
        "P(H)": ph, "P(M)": 1 - ph, "P(FA)": pfa, "P(CR)": 1 - pfa,
        "Z(H)": z_h, "Z(FA)": z_fa,
        "Zsn(기준~SN평균)": -z_h, "Zn(N평균~기준)": -z_fa,
        "f(xc|SN)": N01.pdf(z_h), "f(xc|N)": N01.pdf(z_fa),
        "d'": d_prime, "beta": beta, "ln beta": math.log(beta), "c": c,
        "[표 2자리] d'": zt_h - zt_fa,
        "[표 2자리] beta": N01.pdf(zt_h) / N01.pdf(zt_fa),
    }


def info(m):
    n = sum(map(sum, m))
    check(n == 100, f"행렬 총합 {n} != 100")
    rows = [sum(r) for r in m]
    cols = [sum(c) for c in zip(*m)]
    check(rows == [50, 30, 20], f"행 합 {rows} != 시험지 [50, 30, 20]")
    check(all(v >= 0 for r in m for v in r), "음수 빈도")
    px = [r / n for r in rows]
    py = [c / n for c in cols]
    pxy = [v / n for r in m for v in r]
    check(abs(sum(pxy) - 1) < EPS, "결합확률 합 != 1")
    hx, hy, hxy = entropy(px), entropy(py), entropy(pxy)
    t = hx + hy - hxy
    noise = hxy - hx          # H(Y|X)
    equiv = hxy - hy          # H(X|Y)
    # 검산: 조건부 엔트로피를 정의식으로 직접 계산
    hy_x = sum(px[i] * entropy([v / rows[i] for v in m[i]]) for i in range(3) if rows[i])
    hx_y = sum(py[j] * entropy([m[i][j] / cols[j] for i in range(3)]) for j in range(3) if cols[j])
    check(abs(hy_x - noise) < 1e-9, "H(Y|X) 직접 계산 불일치")
    check(abs(hx_y - equiv) < 1e-9, "H(X|Y) 직접 계산 불일치")
    # 검산: 상호정보량 정의식 Σ p(x,y) log2[p(x,y)/(p(x)p(y))]
    t_direct = sum((m[i][j] / n) * math.log2((m[i][j] / n) / (px[i] * py[j]))
                   for i in range(3) for j in range(3) if m[i][j])
    check(abs(t_direct - t) < 1e-9, "T 직접 계산 불일치")
    check(abs((hy - t) - noise) < 1e-9 and abs((hx - t) - equiv) < 1e-9, "강의 p.59 두 형태 불일치")
    check(-EPS <= t <= min(hx, hy) + EPS, "0 ≤ T ≤ min(H(X),H(Y)) 위반")
    check(noise >= -EPS and equiv >= -EPS, "조건부 엔트로피 음수")
    check(max(hx, hy) <= hxy + EPS and hxy <= hx + hy + EPS, "max(H) ≤ H(X,Y) ≤ H(X)+H(Y) 위반")
    acc = sum(m[i][i] for i in range(3)) / n
    return {
        "행 합": rows, "열 합": cols,
        "H(X)": hx, "H(Y)": hy, "H(X,Y)": hxy, "T(X,Y)": t,
        "Noise H(Y|X)": noise, "Equivocation H(X|Y)": equiv,
        "T/H(X) 전달률": t / hx, "정답 일치율(대각합)": acc,
    }


def lecture_example():
    # 3장 보충 2026.pdf PDF p.60-61 예제로 계산 방식 검증
    m = [[33, 0, 0], [14, 20, 0], [0, 0, 33]]
    n = 100
    rows = [sum(r) for r in m]
    cols = [sum(c) for c in zip(*m)]
    hx = entropy([r / n for r in rows])
    hy = entropy([c / n for c in cols])
    hxy = entropy([v / n for r in m for v in r])
    got = {"H(x)": hx, "H(y)": hy, "H(x,y)": hxy, "T": hx + hy - hxy,
           "손실": hxy - hy, "소음": hxy - hx}
    slide = {"H(x)": 1.585, "H(y)": 1.504, "H(x,y)": 1.917, "T": 1.172,
             "손실": 0.413, "소음": 0.332}
    for k in slide:
        check(abs(got[k] - slide[k]) < 0.0015, f"강의 예제 {k}: {got[k]:.4f} vs {slide[k]}")
    return got, slide


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "work/q2/input.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    print("== 강의 예제 재현 (3장 p.60-61) ==")
    got, slide = lecture_example()
    for k in slide:
        print(f"  {k:8s} 계산 {got[k]:.4f}  슬라이드 {slide[k]}")

    print("\n== (a) SDT ==")
    for name, d in data["sdt"].items():
        print(f"[진단기 {name}]")
        for k, v in sdt(d).items():
            print(f"  {k:20s} {v:.6f}")

    print("\n== (c) 정보량 (bit, log2) ==")
    for name, m in data["info"].items():
        print(f"[진단기 {name}]")
        for k, v in info(m).items():
            print(f"  {k:22s} {v if isinstance(v, list) else f'{v:.6f}'}")

    print("\n== 참고: 기준 최적화 (3장 p.19, p.40) ==")
    p_n, p_s = 800 / 1000, 200 / 1000
    print(f"  오류 최소화 β_opt = P(N)/P(S) = {p_n / p_s:.3f}")
    print("  비용 반영 β* = P(N)/P(S) × (V_CR + C_FA)/(V_H + C_M) — 비용값은 시험지에 없음")

    print("\n== 검산 ==")
    if failures:
        for f in failures:
            print("  실패:", f)
        sys.exit(1)
    print("  모든 검사 통과")


if __name__ == "__main__":
    main()
