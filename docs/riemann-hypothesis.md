# **The Rigorous Mathematical Statement of the Riemann Hypothesis**

The Riemann zeta function $\zeta(s)$ is defined in the complex plane for a complex number $s = \sigma + it$ ($\sigma, t \in \mathbb{R}, i = \sqrt{-1}$) as follows:

## **(1) Definition (Zeta Function)**

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} \quad \text{(for } \sigma = \operatorname{Re}(s) > 1\text{)}
$$

The above series converges absolutely for $\sigma > 1$ and is holomorphic in this domain. Furthermore, it is known that the zeta function can be analytically continued to the entire complex plane, except for a simple pole at $ s = 1 $.

The analytically continued Riemann zeta function $\zeta(s)$ satisfies the following fundamental property:

- **Functional Equation**
  For any $ s \in \mathbb{C} \setminus \{0,1\} $, the zeta function satisfies:

$$
\zeta(s) = 2^s \pi^{s - 1} \sin\left(\frac{\pi s}{2}\right)\Gamma(1 - s)\zeta(1 - s)
$$

From this equation, it follows that the nontrivial zeros of $\zeta(s)$ are symmetrically distributed within the **critical strip** $ 0 < \sigma < 1 $.

---

## **(2) The Riemann Hypothesis (RH)**

$$
\text{"All nontrivial zeros of the Riemann zeta function }\zeta(s)\text{ within the critical strip } 0 < \sigma < 1 \text{ lie on the critical line } \sigma = \frac{1}{2} \text{."}
$$

That is, for any complex number $ s $:

$$
\zeta(s) = 0, \quad 0 < \operatorname{Re}(s) < 1
$$

it must follow that:

$$
\operatorname{Re}(s) = \frac{1}{2}.
$$

---

## **(3) More Rigorous Notation**

For a more formal mathematical expression:

- Let $ Z $ be the set of all nontrivial zeros of the Riemann zeta function:

$$
Z := \{ s \in \mathbb{C} \mid \zeta(s) = 0,\quad 0 < \operatorname{Re}(s) < 1 \}.
$$

Then, the Riemann Hypothesis states that:

$$
\forall s \in Z,\quad \operatorname{Re}(s) = \frac{1}{2}.
$$

---

## **(4) Mathematical Significance**

This rigorous statement asserts that all nontrivial zeros of $\zeta(s)$ align perfectly along a single vertical line in the complex plane. If this is true, it implies an extraordinary degree of order in the distribution of prime numbers, with profound consequences not only for number theory but also for mathematics as a whole—including connections to physics and quantum chaos.

To date, over **tens of trillions** of nontrivial zeros have been computationally verified, and all have been found to lie on the critical line $ \sigma = \frac{1}{2} $. However, a formal proof remains elusive, making it one of the most highly sought-after results in modern mathematics.

---
