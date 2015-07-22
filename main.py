#TODO
#Make this happen. For now, dummy shit. Combat? Turns? That speed thing?
#Spells? A bloody interface?
from cpurpg import *
from characters import *
from copy import deepcopy

dom = Dom()
woon = Yong()
haley = Haley()
nick = Nick()

userparty = party(dom, woon, haley, nick)


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
		while (!q.empty())
			person = q.get()
			if (person.stunD == 0 and person.HP > 0):
				action = int(raw_input("What do you want to do?"))
				person.takeaction(action, baddyparty, userparty)
			person.debuffdown()
			
		
	