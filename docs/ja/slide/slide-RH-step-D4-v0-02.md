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

<!-- スライド 2 -->

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
\Huge 2
$$
---

# 実部と虚部の打ち消し合い

ゼータ関数を展開してみると、  
実部と虚部に分かれる：

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^{\sigma}} \left( \cos(t \log n) - i \sin(t \log n) \right)
$$

---

# 実部（余弦）と虚部（正弦）

- 実部：  

$$
\sum_{n=1}^{\infty} \frac{\cos(t \log n)}{n^{\sigma}}
$$

- 虚部：  

$$
\sum_{n=1}^{\infty} \frac{\sin(t \log n)}{n^{\sigma}}
$$

> これらは**独立した波の重ね合わせ**

---

# ゼロになる条件とは？

ゼータ関数がゼロになるには…

$$
\text{実部も虚部も、同時にゼロ！}
$$

- 波が**ぴったり打ち消し合う**必要がある。
- 無限の波が、1点で静寂をつくる奇跡。

---

# 波の干渉と打ち消し

- 波と波が重なり合うとき：

$$
\text{強め合う？} \quad \text{打ち消す？}
$$

- それぞれの「山」と「谷」が合えば静まる。

> まるで合唱団が、音を打ち消すように。

---

# では、どこで打ち消す？

観察結果から分かっていること：

$$
\mathrm{Re}(s) = \frac{1}{2} のときだけ
$$

- 実部と虚部が**対称に干渉**
- 振動の**位相差が π に一致**

---

# 臨界線の意味

$$
\mathrm{Re}(s) = \frac{1}{2}
$$

ここでは：

- 実部と虚部の波が**鏡像のように対称**
- だから**完璧な打ち消し合い**が可能！

---

# もしずれたら…？

例えば：

$$
\mathrm{Re}(s) = 0.4 \quad \text{や} \quad 0.6
$$

- 波の強さが不均衡
- 位相がずれて**完全には打ち消せない**

---

# 小さなズレが、致命的

- 位相が少しズレるだけで…

$$
\text{合唱団がバラバラに…}
$$

- 結果：**ゼロにならない！**

> 音楽も数学も、調和が命

---

# 結論:打ち消しは臨界線の奇跡

- 無限の波の打ち消し
- その条件は：

$$
\mathrm{Re}(s) = \frac{1}{2}
$$

- 他の値では成立しない

---

# 次へ進もう

- 次の章では：
  - 波の「周期」と「回転」から位相を見ていく
  - オイラー積の観点で「調和と構造」を読み解く
