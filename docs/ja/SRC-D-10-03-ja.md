# SRC-Details (Draft)

cid: 67f77364-91fc-8009-9f61-39e7be5eb077-Euler

---

## 【補強項目：SRC-10-03】

### ディリクレL関数における情報エントロピーの導出：調和構造の定量化

---

### 1. 目的

前節において、L関数の各項が複素調和信号として解釈できることを示した。
本節では、これらの振動項の集合における**調和構造の分布の均質性**を、
**情報理論的エントロピー**の観点から定量化する。

---

### 2. エントロピーの定義と仮定

各項：

\[
a_n(s) := \frac{\chi(n)}{n^s}, \quad |a_n(s)|^2 = \frac{1}{n^{2\sigma}}
\]

を振動強度（構成状態の寄与）とみなし、
それらを確率的寄与としてエントロピーを定義する：

\[
\mathcal{H}_\chi(\sigma) := - \sum_{n=1}^{\infty} |a_n(s)|^2 \log |a_n(s)|^2
= - \sum_{n=1}^{\infty} \frac{1}{n^{2\sigma}} \log \left( \frac{1}{n^{2\sigma}} \right)
\]

ここで \( |\chi(n)| = 1 \) より、構造的には \( \chi \) の有無は振幅に影響せず、
情報エントロピーは次のように簡約される：

\[
\boxed{
\mathcal{H}_\chi(\sigma) = 2\sigma \sum_{n=1}^{\infty} \frac{\log n}{n^{2\sigma}}
}
\]

---

### 3. エントロピー関数の意味

この関数が測定するのは、以下の構造的性質である：

- 各項 \( \chi(n)/n^s \) の**構成的情報寄与の分布**
- 寄与が「高周波（大 \( \log n \)）」に偏っているか、あるいは「低周波」に集中しているか
- 系全体として、**どれだけ調和的に寄与が分散されているか**

ゆえに、エントロピー関数 \( \mathcal{H}_\chi(\sigma) \) の極小点は、
構成項が最も**等調和的に情報寄与する状態**を意味する。

---

### 4. 数論的背景との結合

エントロピー関数の形は、**解析的ゼータ関数の加重和**に他ならない：

\[
\mathcal{H}_\chi(\sigma) = 2\sigma \cdot \frac{d}{d\sigma} \left[ \sum_{n=1}^{\infty} \frac{1}{n^{2\sigma}} \right]
\]

このことは、ゼータ関数そのものが「構造的エントロピー汎関数」を内在していることを意味する。
したがって、臨界線の位置は、単なる解析接続の性質ではなく、**情報構造の最適化点**として解釈可能である。

---

### 5. 結論

- L関数の構造は、ゼータ関数と同様に、**情報エントロピー関数によって調和構造の対称性を測定可能**である。
- その最小点がどこに現れるかは、次節で解析される導関数により明示的に決定される。

---
