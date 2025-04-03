-- ZetaLogic/Phase.lean
import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

open Float

-- 非常にシンプルな素数判定（必要最低限）
def isSmallPrime (n : Nat) : Bool :=
  n > 1 ∧ (List.range (n - 2)).all (λ i => n % (i + 2) ≠ 0)

noncomputable def primePhaseF (p : Nat) (t : Float) : Float :=
  let logp := Float.log (Float.ofNat p)
  let decay := Float.pow (Float.ofNat p) (-0.5)
  Float.atan ((decay * Float.sin (t * logp)) / (1 - decay * Float.cos (t * logp)))

noncomputable def totalPhaseF (bound : Nat) (t : Float) : Float :=
  (List.range bound).filter isSmallPrime
  |>.map (fun p => primePhaseF p t)
  |>.foldl (· + ·) 0.0


def floatPi : Float := 3.141592653589793

noncomputable def isZeroPhaseF (bound : Nat) (t : Float) (ε : Float := 0.01) : Bool :=
  let θ := totalPhaseF bound t
  let m := θ - floatPi * Float.floor (θ / floatPi)  -- mod π 代用
  Float.abs m < ε
