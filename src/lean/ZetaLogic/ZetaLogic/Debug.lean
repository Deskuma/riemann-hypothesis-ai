-- ZetaLogic/Debug.lean
import ZetaLogic.Phase

def checkZeroPhasesAround (bound : Nat) (t0 : Float) : IO Unit := do
  for i in List.range 20 do
    let shift := 0.1 * Float.ofNat i
    let t := t0 + shift
    if isZeroPhaseF bound t then
      IO.println s!"Possible zero phase at t ≈ {t}"
