---
marp: true
theme: uncover
style: |
  section {
    background: #fbfbfb;
    color: #1a1a1a;
    font-family: "Computer Modern", "Times New Roman", serif;
  }
  h1, h2 {
    font-weight: bold;
    color: #003366;
    border-bottom: 2px dotted #aaa;
  }
  code {
    color: #bb0000;
  }
math: mathjax
---

<!-- スライド 1 -->

# リーマン予想に挑む

_数式が描く、数の宇宙を旅しよう_

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}, \quad s = \sigma + it, \quad (\sigma, t \in \mathbb{R})
$$

$$
\mathrm{Re}(s) = \frac{1}{2}
$$

---
$$
\Huge 1
$$
---

# 素数とは？

- 1と自分自身以外に割れない数
- 例：2, 3, 5, 7, 11, 13, ...

> 自然数の「原子」とも言える存在

---

# ゼータ関数の第一歩

中心となる関数：

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}
$$

---

# 分数の大きさって？

$$
\frac{1}{2} > \frac{1}{3} > \frac{1}{4} > \dots > \frac{1}{n} > \dots
$$

- 分母が大きいほど、小さくなる

$$
\frac{2}{2-1} \space ? \space \frac{3}{3-1} \space ? \space \frac{5}{5-1} \space ? \space \dots \space ? \space \frac{p}{p-1}
$$

- **これはどうですか？**

$$
\tiny(2/1) = \normalsize 2.0 >
\tiny(3/2) = \normalsize1.5 >
\tiny(5/4) = \normalsize1.25 > \dots > \left(\frac{n}{n-1}\right) ≈ 1.0
$$

---

# 無限に足し算するとは？

$$
\sum \quad \to \quad 1 + \frac{1}{2} + \frac{1}{3} + \cdots \quad \scriptsize \left(※ \space 1=\frac{1}{1} \right)
$$

- どこまでも小さくなるのに、
- **無限に足すと、どこまでも大きくなる**！？

> これは「発散」

---

# 収束と発散

$$
\sum_{n=1}^{\infty} \frac{1}{n} \to \infty \quad \text{(発散)}
$$
$$
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6} \quad \text{(収束)}
$$

違いは何か？ → **べき指数 s** が影響する！

---

# ゼータ関数の変数 s を考える

$$
s = \sigma + it
$$

- $\sigma$：減衰の強さ（大きさを決める）
- $t$：周期の回転（角度を決める）
- $\vec{s}$ を**ベクトルの矢印**として見ると？ $\overrightarrow{O(0,0) →P(\sigma, t)}$

> これは、**ベクトルの長さと方向**のようなもの

<small>※ベクトルでは**始点座標**はありません。</small>

---

# 項のイメージ：複素ベクトル

$$
\frac{1}{n^s} = \frac{1}{n^{\sigma}} (\cos(t\log n) + i \sin(t\log n))
$$

→ 複素平面上に「矢印」が現れる！

> それらが無限に「繋がって」ゆくとどうなる？

---

# 無限のベクトル和

すべての $n$ に対し、矢印を足し合わせると：

- 渦巻くように進む？
- 打ち消し合って静止する？
- 一方向に吹き続ける？

> これがゼータ関数の振る舞いそのもの！

---

# ゼロになるとは？

$$
\zeta(s) = 0
$$

- 全ての矢印がぴったり**打ち消し合う点**！
- それは、**奇跡的な角度と大きさ**でのみ起こる！

---

# 臨界線とは？

$$
\mathrm{Re}(s) = \frac{1}{2}
$$

- ゼータ関数のすべての**非自明なゼロ**がここにある？
- 本当にそうなのか！？

---

# 次へ

- 「打ち消し合いのメカニズム」を解析する
- 位相、周期、振動の調和へ…
