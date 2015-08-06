

class unit():    
    embossAmount = 0 #emboss amount, because it's easier than passing the party to get Jenny's DEF. It's static
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
        self.embossD = 0 #emboss duration
        self.barrD = 0 #barrier duration

	#returns True if muted
    def checkMute(self):
	if muteD > 0:
    	    return True
        return False
		
	#returns True if bound
    def checkBind(self):
	if bindD > 0:
	    return True
	return False
		
		
    def useSTAM(self, amount):
	if self.STAM < amount:
	    print("not enough stamina to use ability")
	    return False
	self.STAM -= amount
	    return True

    def gainSTAM(self, amount):
	if self.drainD == 0:
	    self.STAM += amount
		if (self.STAM > 10):
		    self.STAM = 10    
		    return True
        else:
	    print("Failed: You are Drained")
	        return False
    
    def heal(self, amount):
        if(self.HP <= 0):
            print "Can't heal outta death"
            return False
        self.HP += amount
        if (self.HP > self.VIT):
            self.HP = self.VIT  
		return True
    
    def levelUp(self):
        self.level += 1
        self.xp = 0 #in theory right? wait shit what about overflow Joe questions.jpg
        self.VIT += VITup
        self.STR += STRup
        self.INT += INTup
        self.DEF += DEFup 
	def attack(self, target):
		if not checkBind():
			if self.STR - target.DEF > 0
				target.HP -= (self.STR - target.DEF)
			return True
		return False
	def debuffdown(self):
		if self.bindD > 0:
		    self.bindD -= 1
		if self.stunD > 0:
		    self.stunD -= 1
		if self.drainD > 0:
		    self.drainD -= 1
		if self.muteD > 0:
	            self.muteD -= 1
                if self.barrD > 0: #Kenji's barrier
                    self.barrD -= 1
                    if (self.barrD == 0):
                        self.DEF -= 5
                if self.embossD > 0: #Jenny's def buff
                    self.embossD -= 1
                    if (self.embossD == 0):
                        self.DEF -= embossAmount

	def takeaction(self, i, baddyparty, userparty):
		if i == 1:
			Nexecuted = True
			while(Nexecuted):
				target = int(raw_input("Who do you want to attack? "))
				if target == 1 or target == 2:
					attack(baddyparty[i - 1])
					Nexecuted = False;
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
