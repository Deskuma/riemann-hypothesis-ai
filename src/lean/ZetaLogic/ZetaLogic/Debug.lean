-- ZetaLogic/Debug.lean
import ZetaLogic.Phase

noncomputable def checkZeroPhasesAround (bound : Nat) (t0 : Float) (steps : Nat := 20) (delta : Float := 0.1) : IO Unit := do
  for i in List.range steps do
    let shift := delta * Float.ofNat i
    let t := t0 + shift
    if isZeroPhaseF bound t then
      IO.println s!"Possible zero phase at t ≈ {t}"
