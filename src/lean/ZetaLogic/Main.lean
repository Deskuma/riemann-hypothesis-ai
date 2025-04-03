import ZetaLogic.Basic

def main : IO Unit := do
  let result := partialZetaSumF 1000 14.1347
  IO.println s!"Zeta sum: {result.re} + {result.im}i"

-- Main.lean
