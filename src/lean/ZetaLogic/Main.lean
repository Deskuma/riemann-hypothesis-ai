import ZetaLogic.Basic
import ZetaLogic.Debug

noncomputable def main : IO Unit := do
  let result := partialZetaSumF 1000 14.1347
  IO.println s!"Zeta sum: {result.re} + {result.im}i"
  IO.println s!"Scanning for phase cancellations near known zero:"
  checkZeroPhasesAround 100 14.0
