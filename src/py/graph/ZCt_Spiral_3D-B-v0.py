# ZC(t) Spiral Interference Split: 3D Visualization of Symmetric Spiral Pair
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpmath as mp
from sympy.ntheory.primetest import isprime

mp.dps = 50


# Z[i] 内の複素素数（ノルム上限）
def gaussian_primes(max_norm):
    results = []
    for a in range(-max_norm, max_norm + 1):
        for b in range(-max_norm, max_norm + 1):
            if a == 0 and b == 0:
                continue
            n = a**2 + b**2
            if isprime(n):
                results.append(complex(a, b))
    return results


gprimes = gaussian_primes(10)

# ベクトル生成（ZC要素）
t_vals = np.linspace(0, 40, len(gprimes))
vectors = []
for i, pi in enumerate(gprimes):
    norm = abs(pi)
    log_norm = mp.log(norm)
    t = t_vals[i]
    term = (1 / mp.sqrt(norm)) * mp.exp(-1j * t * log_norm)
    vectors.append(term)

# 2分割して対称構成
half = len(vectors) // 2
vec1 = vectors[:half]
vec2 = [-v for v in vec1[::-1]]  # 対称逆向き

# 螺旋Aの累積和
points1 = [mp.mpc(0)]
for v in vec1:
    points1.append(points1[-1] + v)

# 螺旋BのスタートはAの終端から始める（干渉観察）
start_point2 = points1[-1] + vec1[-1]
points2 = [start_point2]
for v in vec2[:-1]:
    points2.append(points2[-1] + v)


# numpy 変換 + t 軸付加
def mp_to_3d(points, t_vals):
    return np.array(
        [[float(p.real), float(p.imag), float(t)] for p, t in zip(points, t_vals)]
    )


mid_t_vals = np.linspace(0, 20, len(points1))
points1_np = mp_to_3d(points1, mid_t_vals)
points2_np = mp_to_3d(points2, mid_t_vals)

# 3D プロット（スパイラルAと対称スパイラルB）
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

ax.plot(
    points1_np[:, 0],
    points1_np[:, 1],
    points1_np[:, 2],
    color="blue",
    linewidth=1.5,
    label="Spiral A",
)
ax.plot(
    points2_np[:, 0],
    points2_np[:, 1],
    points2_np[:, 2],
    color="red",
    linestyle="--",
    linewidth=1.5,
    label="Spiral B",
)

ax.scatter([0], [0], [0], color="green", s=40, label="Start (0, 0, 0)")
ax.scatter(
    points2_np[-1, 0],
    points2_np[-1, 1],
    points2_np[-1, 2],
    color="orange",
    s=40,
    label="End",
)

ax.set_title("ZC(t) Interference Spiral in 3D (Split Re, Im, t)")
ax.set_xlabel("Re")
ax.set_ylabel("Im")
ax.set_zlabel("t")
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()

print("Final interference endpoint:")
print(points2[-1])
