#TODO
#Make this happen. For now, dummy shit. Combat? Turns? That speed thing?
#Spells? A bloody interface?
from cpurpg import *

unitA = unit("A", 1, 0, 100, 5, 5, 5, 100, 5)
unitB = unit("B", 1, 0, 100, 5, 5, 5, 100, 5)
unitC = unit("C", 1, 0, 100, 5, 5, 5, 100, 5)
unitD = unit("D", 1, 0, 100, 5, 5, 5, 100, 5)

baddies1 = unit("Baddies", 1, 0, 10, 2, 2, 2, 10, 4)
baddies2 = unit("Baddies", 1, 0, 10, 2, 2, 2, 10, 4)
baddies3 = unit("Baddies", 1, 0, 10, 2, 2, 2, 10, 4)
baddies4 = unit("Baddies", 1, 0, 10, 2, 2, 2, 10, 4)

userParty = party(unitA, unitB, unitC, unitD)
baddyParty = party(baddies1, baddies2, baddies3, baddies4)

userParty.statquery(0)
