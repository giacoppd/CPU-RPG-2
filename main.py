#TODO
#Make this happen. For now, dummy shit. Combat? Turns? That speed thing?
#Spells? A bloody interface?
from cpurpg import *
from copy import deepcopy

unitA = unit("A", 1, 0, 100, 5, 5, 5, 100, 5)
unitB = unit("B", 1, 0, 100, 5, 5, 5, 100, 5)
unitC = unit("C", 1, 0, 100, 5, 5, 5, 100, 5)
unitD = unit("D", 1, 0, 100, 5, 5, 5, 100, 5)

baddies1 = unit("Baddies", 1, 0, 10, 2, 2, 2, 10, 4)
baddies2 = unit("Baddies", 1, 0, 10, 2, 2, 2, 10, 4)
baddies3 = unit("Baddies", 1, 0, 10, 2, 2, 2, 10, 4)
baddies4 = unit("Baddies", 1, 0, 10, 2, 2, 2, 10, 4)

userparty = party(unitA, unitB, unitC, unitD)
baddyparty = party(baddies1, baddies2, baddies3, baddies4)

userParty.statquery(0)

def instance(userparty, baddyparty):
	x = 0
	q = Queue()
	allpeeps.partylist = deepcopy(userparty.partylist)
	allpeeps.partylist.append(baddyparty.partylist)
	sorted(allpeeps.partylist, key=spd, reverse=TRUE)
	while true:
		for person in allpeeps.partylist:
			if x % (60 / person.spd) == 0:
				q.put(person)
		for person in q:
			q.get()
			action = int(raw_input("What do you want to do?"))
			#execute action
			
		
	