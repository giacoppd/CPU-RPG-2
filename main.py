#TODO
#Make this happen. For now, dummy shit
from cpurpg import *

unitA = unit("A", 1, 0, 100, 5, 5, 5, 100, 5)
unitB = unit("B", 1, 0, 100, 5, 5, 5, 100, 5)
unitC = unit("C", 1, 0, 100, 5, 5, 5, 100, 5)
unitD = unit("D", 1, 0, 100, 5, 5, 5, 100, 5)

userParty = party(unitA, unitB, unitC, unitD)
#userParty.statquery(userParty.partylist[0])
userParty.statquery(0)
