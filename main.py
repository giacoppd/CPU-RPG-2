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
	for person in allpeeps.partylist:
		if person.spd == 6:
			if x == 0 or x == 1 or x == 4 or x == 6 or x == 8 or x == 11:
				q.put(person)
		else if person.spd == 5:
			if x == 0 or x == 2 or x == 5 or x == 7 or x == 10:
				q.put(person)
		else if person.spd == 4:
			if x % 3 == 0:
				q.put(person)
		else if person.spd == 3:
			if x % 4 == 0:
				q.put(person)
		else if person.spd == 2:
			if x % 6 == 0:
				q.put(person)
	for person in q:
		q.get()
	