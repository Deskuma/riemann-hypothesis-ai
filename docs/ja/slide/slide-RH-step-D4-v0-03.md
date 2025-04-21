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

<!-- スライド 3 -->

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
\Huge 3
$$
---

# スケールと位相の観点

ゼータ関数の振動には、
2つの重要な成分がある：

- **スケール（大きさ）**
- **位相（角度）**

---

# スケール関数

波の「大きさ」を決める：

$$
\text{scale}(t) = \sum_{n=1}^{\infty} \frac{\cos(t \log n)}{\sqrt{n}}
$$

- 実部に対応
- 小さい数ほど大きな寄与

---

# 位相角関数

波の「回転方向」を決める：

$$
\text{angle}(t) = -\sum_{n=1}^{\infty} \frac{\sin(t \log n)}{\sqrt{n}}
$$

- 虚部に対応
- 回転しながら足されるベクトル

---

# スケールと位相の打ち消し

両方の成分が
**同時にゼロ**になれば…

$$
\zeta(s) = 0
$$

- それには**絶妙な調和**が必要！

---

# 零点の成立条件

次の2つが同時に成り立つとき：

$$
\sum_{n=1}^{\infty} \frac{\cos(t \log n)}{\sqrt{n}} = 0
$$
$$
\sum_{n=1}^{\infty} \frac{\sin(t \log n)}{\sqrt{n}} = 0
$$

> この2つの和は、完全に打ち消し合う瞬間を意味する

---

# なぜ臨界線か？

$$
\mathrm{Re}(s) = \frac{1}{2} のとき
$$

- 実部と虚部の大きさが**完全に対称**
- スケールと位相の**振動がちょうど π の位相差**になる

---

# それ以外の s では？

$$
\mathrm{Re}(s) \ne \frac{1}{2}
$$

- 実部と虚部の**振動バランスが崩れる**
- 一方だけが強すぎて**打ち消し不可能**になる

---

# 可視化すると？

- グラフでは：

  - 実部：ずれて軌跡がゆがむ
  - 虚部：振動の中心から外れる

> まるで「チューニングが外れた楽器」のよう

---

# 臨界線は「調和」の場所

- $\sigma = \frac{1}{2}$ は、波が互いに**最もよく干渉し、最もよく静まる位置**
- それ以外では**調和が崩れる**

---

# 次へ

次章では：

- 実際に図やアニメーションでこの現象を観察
- 視覚的に「なぜ π の位相差が特別なのか」を確認
