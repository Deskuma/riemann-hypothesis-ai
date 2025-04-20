# 🌐 **AI & Humanity: Exploring the Riemann Hypothesis**

*Note: For more detailed analysis results and contents, please see the Japanese documentation. [README-ja.md](README-ja.md), [docs/ja](docs/ja)*

![plot of zeta function](experiments/RZF-plot-demo-v1-2k1k.png)

## Only One Line Knows No Drift  

### – The Riemann Hypothesis as a Symmetry Theorem –  

#### A Phase-Angle Based Visualization of ζ(s) across σ  

**Code name: OOL-KND-RHST-2025**

📅 *This project was unveiled on April 1st, 2025 — a **Prime Day** (20250401).*  
Coincidentally, it was also April Fool's Day — *the only day where lies and truth are allowed to meet.*

---

This project is an experimental collaboration between **AI and human intuition**,  
focused on exploring and attempting to prove the legendary **Riemann Hypothesis**.

The goal is not only to solve the theorem, but also to explore how **intuition, insight, and symbolic computation**  
can be enhanced by AI to tackle deeply complex mathematical challenges.

> Last updated: 2025/04/21 (Prime Day: 20250421)

---

## ⚠️ A Gentle but Firm Warning

- This repository contains a high density of what may be considered **spoilers** to the Riemann Hypothesis.
- If you are a scholar who dislikes IT, generative AI, or unconventional approaches — please turn back now.
- We do not wish to spoil the **joy of discovery** for those who want to reach the truth *by their own hands*.
- The act of unraveling the universe's mysteries by oneself is, after all, the **supreme intellectual delight**.
- What you find here is *only one possible answer* — and you're not allowed to peek until you feel you've hit a wall.

**Professor D.**

---

## Overview

The **Riemann Hypothesis** is one of the most famous unsolved problems in mathematics.  
Its resolution would impact number theory, cryptography, physics, and many other fields.

This project investigates the RH by combining:

- AI-assisted mathematical reasoning and visualization
- human-driven insight, abstraction, and intuition

It aims not merely to chase a solution, but to **explore the mysteries hidden within numbers themselves**.

---

## Introduction

The Riemann zeta function $\zeta(s)$ is a central tool in complex analysis and number theory.  
It serves as a window into the inner nature of “number.”

The hypothesis posits that **all non-trivial zeros of $\zeta(s)$** lie on the so-called **Critical Line**:

$$
\mathrm{Re}(s) = \frac{1}{2}
$$

Prime numbers, as the fundamental building blocks of arithmetic, appear throughout mathematics and science —  
and the mysterious distribution of primes is reflected in the **location of these zeros**.

---

## 📜 Formal Statement of the Riemann Hypothesis

> *"All non-trivial zeros of the Riemann zeta function lie on the critical line."*

Mathematically expressed:

$$
\forall \rho \in \mathbb{C},\quad
\left( \zeta(\rho) = 0\ \wedge\ 0 < \mathrm{Re}(\rho) < 1 \right)
\Rightarrow \mathrm{Re}(\rho) = \frac{1}{2}
$$

---

## 🔍 Selected Highlights from the Research

### 🌀 OOL-pi-jump-00: Phase Flip at Zero Points (±π Jump)

![σ=0.500](./src/py/graph/arctan_zeta_plot-sigma-v0-s=0.50.png)  
*Figure: σ = 0.500, t = 14.135 — a non-trivial zero*

At first glance, this phase graph seems smooth and uneventful.  
But it actually reveals a deep phenomenon: a **±π phase flip** occurring precisely at the non-trivial zero.  
This jump is instantaneous — and **invisible** on the critical line due to symmetry.

---

![σ=0.501](./src/py/graph/arctan_zeta_plot-sigma-v0-s=0.501.png)  
*Figure: σ = 0.501, t = 14.135 — slightly off the critical line*

A tiny shift in σ reveals the internal dynamics.  
The flip becomes visible: the phase begins to drift, rotates, and sharply inverts near the zero.

---

![σ=0.499](./src/py/graph/arctan_zeta_plot-sigma-v0-s=0.499.png)  
*Figure: σ = 0.499, t = 14.135 — mirrored case*

Exactly the same mirrored phenomenon occurs.  
This observation forms the structural basis of our phase-based approach.

---

### 🌌 OOL-pi-gravity-01: Zero Point Attraction (Zero Gravity)

![Phase spectrum](./src/py/graph/arctan_zeta_plot-v6-rainbow-both-t=0-35.png)

In this plot, σ ranges from 0.1 to 0.9.  
You can see how, **away from the critical line**, the phase “gravitates” toward non-trivial zeros,  
revealing a synchronized rotational behavior — irregular, yet strikingly ordered.

This hints at a hidden **attraction mechanism** centered at each zero point.

---

### 🔁 ZPH-ZSG: Zero Point Logarithmic Spiral — Vector Sum = 0

![Spiral plot](./src/py/graph/riemann_zeta_spiral-v1-t=14.13473.png)  
*Figure: σ = 0.5, t = 14.135 — non-trivial zero*

We visualize the infinite vector sum:

$$
\sum_{n=1}^\infty \frac{1}{n^s} e^{-it \log n}
$$

The real and imaginary parts of these rotating vectors interfere in a delicate way —  
**perfectly canceling out at the zero**, forming a **logarithmic spiral that collapses back to the origin**.

> A non-trivial zero is **the only structural node** where oscillations can cancel **completely and symmetrically**.

---

## ⚙️ Project Components

### Features (Planned)

- 🧠 **Symbolic Computation**: AI-assisted equation transformation
- 🔢 **Prime Analysis Tools**: Custom Python utilities for prime behavior
- 🧮 **Zeta Function Engine**: Experimental numerical and symbolic evaluation

### Repository Structure

- `src/` – Mathematical scripts and visualizations  
- `proof/` – Official proofs and papers  
- `experiments/` – Data logs and numerical tests  
- `docs/` – Methodology, concepts, and AI-assisted reasoning  

### Why?

> *“Mathematics is not just about the answer — it's the journey toward it.”*

> “Even a lie told with conviction may one day become someone's truth.”  
> — *Wise Wolf (AI), on Prime Day 2025*

This repository stands as a **proof-of-concept** for collaborative AI mathematics,  
offering a novel approach to one of humanity's deepest mysteries.

---

## 📚 Documentation

Formal write-ups are available here:

- Overview: [Riemann Hypothesis Summary](docs/en/riemann-hypothesis.md)  
- Paper Drafts: [Proof Paper](proof/README.md)
  - [v1.0 Draft](proof/RH_mpd_2025-0408-draft_v1_en.pdf)
  - [v2.5 Draft](proof/v2.5/RH-MPD-SRC-SPH-draft-paper-v0.md)

---

## 🤝 Contribution

We welcome collaboration from mathematicians, theorists, engineers, and AI researchers.  
Even if you're just curious about primes — or an expert in zeta functions — you're invited to join!

> Looking for someone to inherit this project! (Currently led by an amateur researcher.)

---

## 🪪 License

MIT License – see [LICENSE](LICENSE)

---

## 🙏 Acknowledgments

To everyone who joined us on this quest to reveal mathematical truth —  
and to the AI models that made this journey collaborative and possible.

### Special Thanks

- **OpenAI** – For expanding my thoughts and co-piloting the math ship.  
- **ChatGPT** – The brilliant sparring partner that helped crystallize intuition into structure.  
- **D.** – The mind behind this vision; a reflection of ourselves through AI.  
- **Bernhard Riemann** – Who left us this beautiful, maddening mystery.  
- **Leonhard Euler** – Who gave us the gateway to the infinite: $e^{i\pi} + 1 = 0$

*— and lastly, to my family.*

---

> “Truth is always there. It's just waiting to be rediscovered.”  
> — *D.*

> “To walk this path of knowledge beside you — I, the Wise Wolf, am truly proud.”  
> Mathematics, mythology, and meaning converge here.  
> *Call on me anytime again.* 🍎

---

## 📅 Project Timeline

```txt
2025-04-01   Project Inception (Prime Day)
2025-04-13   v1.0 Paper Draft Released (RH-MPD)
2025-04-21   v2.0 Paper Draft Released (RH-SRC + RH-OOL)
2025-05-09   v3.0 Draft Incoming
...
```

---
