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

<!-- スライド 6 -->

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
\Huge 6
$$
---

# ゼロ点の謎

ゼータ関数の非自明なゼロは…

- ランダムなようで、
- 全てが **直線上** に並んでいる！

$$
\mathrm{Re}(s) = \frac{1}{2}
$$

なぜ？

---

# 無限の「干渉系」

ゼータ関数とは…

- 無限のベクトルが重なり合う**干渉の場**
- それらがぴったり打ち消し合う → ゼロ点！

$$
\zeta(s) = 0 \quad \Longleftrightarrow \quad \text{完全な destructive interference}
$$

---

# 複素指数の位相構造

1つの項：

$$
n^{-s} = n^{-\sigma} e^{-it \log n}
$$

→ 矢印の回転と大きさ

全体：

$$
\sum_{n=1}^\infty n^{-s} = \text{複素平面上の矢印の和}
$$

---

# 臨界線の意味

$$
\mathrm{Re}(s) = \frac{1}{2}
$$

- 減衰（スケール）と回転（位相）が**ちょうど釣り合う**
- それ以外では → バランス崩壊！

> **調和点＝臨界線**

---

# 零点が整列する理由

- 無限に多くの項が、**同時にゼロを作れるのは臨界線上だけ**
- 他の位置では矛盾・干渉崩壊が起きる

→ ゼータ関数の「最小エネルギー状態」はここ！

---

# 波としての視点

各項は振動する波：

$$
\cos(t \log n), \quad \sin(t \log n)
$$

臨界線上では、これらが

- 対称的に反転し
- ゼロに収束する構造を持つ！

---

# オーケストラの比喩

ゼータ関数は、無限の楽器による合奏

- 臨界線上 → 全ての音が「静寂」を生む
- 他の場所 → ノイズ・カオスが残る

---

# 結論：整列するゼロ点

- ランダムに見えるが、実は**超高精度で整列**
- ゼータ関数が許す唯一の**打ち消し構造**がそこにある

---

# 次へ：整数と素数の深い構造へ

ここまでで見たことをふまえ…

- 「整数と素数の構造」
- 「新たな関係式」
- 「調和的構造としての数論」

へ進みます！
