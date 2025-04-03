-- ZetaLogic/Basic.lean

-- ★ 不要な import を削除 ★
-- import Mathlib.Data.Complex.Exponential
-- import Mathlib.Analysis.SpecialFunctions.Complex.Log
-- import Mathlib.Analysis.SpecificLimits.Basic

-- open Complex Real も使わない方が安全

structure ComplexF where
  re : Float
  im : Float
deriving Repr

instance : Add (ComplexF) where
  add a b := ⟨a.re + b.re, a.im + b.im⟩

def expF (z : ComplexF) : ComplexF :=
  let r := Float.exp z.re
  ⟨r * Float.cos z.im, r * Float.sin z.im⟩

def zetaVectorF (n : Nat) (t : Float) : ComplexF :=
  if n = 0 then ⟨0.0, 0.0⟩ else
    let n_sqrt := Float.sqrt (Float.ofNat n)
    let logn := Float.log (Float.ofNat n)
    let θ := -t * logn
    let z := ⟨0.0, θ⟩
    let e := expF z
    ⟨(1.0 / n_sqrt) * e.re, (1.0 / n_sqrt) * e.im⟩

def partialZetaSumF (N : Nat) (t : Float) : ComplexF :=
  (List.range N).map (λ n => zetaVectorF (n + 1) t) |>.foldl (· + ·) ⟨0.0, 0.0⟩
