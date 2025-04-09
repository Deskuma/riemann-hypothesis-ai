# ZC(t) Spiral Symmetric Split Experiment + 3D Visualization
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

# 累積ベクトル座標 + t 軸で 3D 化
points = [mp.mpc(0)]
for v in vectors:
    points.append(points[-1] + v)


# numpy 変換 + t 軸付加
def mp_to_3d(points, t_vals):
    return np.array(
        [
            [float(p.real), float(p.imag), float(t)]
            for p, t in zip(points, [0] + list(t_vals))
        ]
    )


points_np = mp_to_3d(points, t_vals)

# 3D プロット
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

ax.plot(
    points_np[:, 0],
    points_np[:, 1],
    points_np[:, 2],
    color="navy",
    linewidth=1.5,
    label="ZC Spiral 3D",
)
ax.scatter([0], [0], [0], color="green", s=40, label="Start (0, 0, 0)")
ax.scatter(
    points_np[-1, 0], points_np[-1, 1], points_np[-1, 2], color="red", s=40, label="End"
)

ax.set_title("ZC(t) Spiral in 3D (Re, Im, t)")
ax.set_xlabel("Re")
ax.set_ylabel("Im")
ax.set_zlabel("t")
ax.legend()
ax.grid(True)

plt.tight_layout()
plt.show()

print("Final 3D vector position:")
print(points_np[-1])
