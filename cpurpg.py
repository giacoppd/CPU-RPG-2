

class unit():
    def __init__(self, name, level, xp, VIT, STR, INT, DEF, STAM, SPD, VITup, STRup, INTup, DEFup):
        self.level = level
	self.name = name
        self.xp = xp
        self.HP = VIT
        self.VIT = VIT
        self.STR = STR
        self.INT = INT
        self.DEF = DEF
        self.STAM = STAM
        self.SPD = SPD #if speed is tied, highest current STAMinia goes first
        self.stunD = 0 #stun duration, mute, bind, drain
        self.muteD = 0
        self.bindD = 0
        self.drainD = 0
        self.VITup = VITup
        self.STRup = STRup
        self.INTup = INTup
        self.DEFup = DEFup

    def useSTAM(amount):
		if self.STAM < amount:
			print("not enough stamina to use ability")
			return false;
        self.STAM -= amount

    def gainSTAM(amount):
        self.STAM += amount
        if (self.STAM > 10):
            self.STAM = 10    
    
    def heal(amount):
        self.HP += amount
        if (self.HP > self.VIT):
            self.HP = self.VIT  
    
    def levelUp(self):
        self.level += 1
        self.xp = 0 #in theory right? wait shit what about overflow Joe questions.jpg
        self.VIT += VITup
        self.STR += STRup
        self.INT += INTup
        self.DEF += DEFup 
	def attack(target):
		target.HP -= (self.STR - target.DEF)
	def debuffdown():
		if bindD > 0:
			bindD -= 1
		if stunD > 0:
			stunD -= 1
		if drainD > 0:
			drainD -= 1
		if muteD > 0:
			muteD -= 1
	def takeaction(i, baddyparty, userparty):
		if i == 1:
			executed = false
			while(!executed):
				target = int(raw_input("Who do you want to attack? "))
				if target == 1 or target == 2:
					attack(baddyparty[i - 1])
					executed = true;
				else:
					print("Invalid target")
					


class party():

    def __init__(self, A, B, C, D): #create a party and assign to it
        self.partylist = []
        self.partylist.append(A)
	self.partylist.append(B)
	self.partylist.append(C)
	self.partylist.append(D)

    def memSwap(self, slot, roster, rosterSlot): #slot is the position to change, roster is the overall player roster, rosterSlot is their location in the roster
        unit dummy = self.partylist[slot]
        self.partylist[slot] = roster[rosterSlot]
        roster[rosterSlot] = dummy
#TODO make roster a thing overall. Just a global list of all the players not in the main party

    def statquery(self, num): #may or may not be useful
        form = '{stat:8} {val:8}'
        print form.format(stat = 'LEVEL', val = self.partylist[num].level)
        print form.format(stat = 'XP', val = self.partylist[num].xp)
        print form.format(stat = 'VIT', val = self.partylist[num].VIT)
        print form.format(stat = 'STR', val = self.partylist[num].STR)
        print form.format(stat = 'INT', val = self.partylist[num].INT)
        print form.format(stat = 'DEF', val = self.partylist[num].DEF)
        print form.format(stat = 'STAMINA', val = self.partylist[num].STAM)
        print form.format(stat = 'SPD', val = self.partylist[num].SPD)
