# **Formal Proof: Phase Cancellation and Zero Conditions**

この条件を成すためには、偶関数と奇関数の位相差、位相角が 1/2
つまり $2π$ の半分 $π$ となる必要があります。

どうです？ $π$ ですよ。なんと美しき事か✨️

その $π$ を成立させるのが実部 $\mathrm{Re}(s)=\frac{1}{2}$ のみなのです。

1. スケール関数の定義

積表示では、

$$
\text{scale}(\theta) = \frac{\sqrt{p}}{| \sqrt{p} e^{i \theta} - 1 |}
$$

総和表示では、**スケール成分は「ゼータ関数の実部」に相当する。**
つまり、

$$
\text{scale}(t) = \sum_{n=1}^{\infty} \frac{\cos(t \log n)}{\sqrt{n}}
$$

これは、**個々の項が素数の影響を受けながら、調和振動を起こしていることを示す**。

2. 位相角関数の定義

積表示では、

$$
\text{angle}(\theta) = \arg\left( \frac{e^{i \theta}}{\sqrt{p} e^{i \theta} - 1} \right)
$$

総和表示では、**位相角成分は「ゼータ関数の虚部」に相当する。**
つまり、

$$
\text{angle}(t) = - \sum_{n=1}^{\infty} \frac{\sin(t \log n)}{\sqrt{n}}
$$

3. 位相相殺の確認

積表示では、**位相差が $ \pi $ になることでゼロ点が形成される** ことを確認した。
総和表示では、**実部と虚部の振動がちょうど打ち消し合う点** がゼロ点となる。

つまり、

$$
\sum_{n=1}^{\infty} \frac{\cos(t \log n)}{\sqrt{n}} = 0
$$

$$
\sum_{n=1}^{\infty} \frac{\sin(t \log n)}{\sqrt{n}} = 0
$$

が同時に成り立つ $ t $ がゼロ点の条件となる。

この式は、**積表示における「スケールと位相角の打ち消し」に対応** するものである。

4. 総和表示の周期性

積表示では、周期が

$$
T = \frac{2\pi}{\log p}
$$

であった。
総和表示でも、$ t $ の変化が $ \frac{2\pi}{\log n} $ の倍数になると周期が繰り返される。

よって、

$$
t \to t + \frac{2\pi}{\log n}
$$

のとき、ゼータ関数のスケールと位相角の振る舞いが周期的に繰り返される。

5. ゼロ点の発生条件

積表示では、スケールと位相角が **逆位相（πの位相差）** になることがゼロ点の条件であった。

総和表示では、実部と虚部の振動が完全に打ち消し合う点がゼロ点となる。
つまり、ゼロ点の条件は、

$$
\sum_{n=1}^{\infty} \frac{e^{-i t \log n}}{\sqrt{n}} = 0
$$

これは、

$$
\sum_{n=1}^{\infty} \frac{\cos(t \log n)}{\sqrt{n}} = 0
$$

$$
\sum_{n=1}^{\infty} \frac{\sin(t \log n)}{\sqrt{n}} = 0
$$

が同時に成り立つことと等価である。
この結果は、積表示で示した位相相殺と完全に一致している！

---

[←index](../README.md)
[Prev: Key Focus of the Proof](how-to-prove-the-riemann-hypothesis-step-03.md) | [Next: ???](how-to-prove-the-riemann-hypothesis-step-05.md)
