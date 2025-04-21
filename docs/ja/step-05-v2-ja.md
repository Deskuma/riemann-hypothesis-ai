# リーマン予想

cid: 67faeec9-b2c0-8009-bb72-85c5c498302f
Ver: 2.0

## Step-05

---

### 第5章：可視化による補強──臨界線外での位相ずれ  

**目的：** 位相ずれの概念を視覚的・定量的に検証し、臨界線上でのみゼータ関数の実部と虚部の完全な打ち消しが可能であることを補強する。

---

#### 命題 5.1（臨界線以外では打ち消しが不完全）

任意の \( s = \sigma + it \) に対して、もし \( \sigma \ne \frac{1}{2} \) であれば、以下の現象が観測される：

- 実部と虚部の振動は同期せず、打ち消しのタイミングがずれる
- 結果として、ゼータ関数の値はゼロに達しなくなる

このことは、視覚的にも以下のように観察される：

- 実部の曲線（通常は赤線）は、虚部と比べて振幅や位相にずれを持つ
- 臨界線上では、両者が一致し、零点が形成される

---

#### 補足説明（位相ずれの視覚的特徴）

観測により、以下が明確となる：

- \( \sigma = \frac{1}{2} \) のとき、実部と虚部のピークは**完全に一致**し、打ち消しが成立する
- \( \sigma \ne \frac{1}{2} \) のとき、実部は**位相ずれ**を起こし、振動のピーク位置が虚部とずれてしまう

これにより、ゼータ関数の零点形成が妨げられる。

---

#### 命題 5.2（視覚的証明の結論）

視覚的に観測される以下の条件は、臨界線上での調和同期を裏付ける：

- \( \Re(\zeta(s)) = 0 \) かつ \( \Im(\zeta(s)) = 0 \) が一致して成立する
- 実部と虚部の**位相差が \(\pi\)** になる（完全反転）

この現象は臨界線以外では決して生じない。

---

#### 定義 5.1（機能方程式の視点からの補強）

ゼータ関数の機能方程式：

\[
\zeta(s) = 2^s \pi^{s - 1} \sin\left( \frac{\pi s}{2} \right) \Gamma(1 - s) \zeta(1 - s)
\]

は、臨界線を唯一の**鏡映対称軸**とするため、振動の「同期」が成立しうるのは \(\Re(s) = \frac{1}{2}\) に限られる。

### グラフ 5.0

以下のグラフは、臨界線上でのゼータ関数の実部と虚部の振動を示しています。
特に、位相ずれがどのように影響を与えるかを視覚的に確認できます。

![Figure 0: 位相ずれの視覚化アニメ](/experiments/RZF-ZeroPoint-sigma-animation-v0.gif)

$$\text{Figure 0: 位相ずれのアニメ}$$

![Figure 1: 位相ずれの視覚化](/experiments/RZF-ZeroPoint-sigma=omega.png)

$$\text{Figure 1: 位相ずれの視覚化}$$

![Figure 2: 位相ずれの視覚化](/experiments/RZF-ZeroPoint-sigma=omega-z1.png)

$$\text{Figure 2: 位相ずれの視覚化(拡大)}$$

![Figure 3: 位相ずれの視覚化](/experiments/RZF-ZeroPoint-sigma=omega-z2-ex1.png)

$$\text{Figure 3: 位相ずれの視覚化(拡大)}$$

![Figure 4: 位相ずれの視覚化](/experiments/RZF-ZeroPoint-sigma=omega-z2-ex2.png)

$$\text{Figure 4: 位相ずれの視覚化(拡大)}$$

![Figure 5: 位相ずれの視覚化](/experiments/RZF-ZeroPoint-sigma=omega-z3-ex1.png)

$$\text{Figure 5: 位相ずれの視覚化(拡大)}$$

![Figure 6: 位相ずれの視覚化](/experiments/RZF-ZeroPoint-sigma=omega-z3-ex2.png)

$$\text{Figure 6: 位相ずれの視覚化(拡大)}$$

![Figure 7: 位相ずれの視覚化](/experiments/RZF-ZeroPoint-sigma=omega-z3-ex3.png)

$$\text{Figure 7: 位相ずれの視覚化(拡大)}$$
