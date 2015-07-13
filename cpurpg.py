class spell():
    def __init__(self, typ, aoe):
      self.typ = typ #either phys, which is reduced by def + str, magic, reduced by def + int, pure, no reductions, or a non-damage
      #TODO
      #We need to feed it the list of spells joe has. It's going to suck. Just a lot of variety in here.

class unit():
    def __init__(self, name, level, xp, vit, STR, INT, DEF, stam, spd):
        self.level = level
	self.name = name
        self.xp = xp
        self.vit = vit
        self.STR = STR
        self.INT = INT
        self.DEF = DEF
        self.stam = stam
        self.spd = spd #if speed is tied, highest current staminia goes first
        self.stunD = 0 #stun duration, mute, bind, drain
        self.muteD = 0
        self.bindD = 0
        self.drainD = 0
    
    def usespell(spellNum): #needs work, maybe just can it for hardcoded spells?
        target = raw_input ("Select target: ")
        svit -= spelllist[spellselect].svit
        sstr -= spelllist[spellselect].sstr
        sint -= spelllist[spellselect].sint
        main[target].sdef -= spelllist[spellselect].sdef
        main[target].sstam -= spelllist[spellselect].sstam
        main[target].sspd -= spelllist[spellselect].sspd
        main[target].sstun -= spelllist[spellselect].sstun
        main[target].sdrain -= spelllist[spellselect].sdrain
        main[target].sbind -= spelllist[spellselect].sbind
        main[target].smute -= spelllist[spellselect].smute

class party():
    def __init__(self, A, B, C, D): #create a party and assign to it
        self.partylist = []
        self.partylist.append(A)
	self.partylist.append(B)
	self.partylist.append(C)
	self.partylist.append(D)
    def memSwap(self, slot, newMem): #slot is the position to change, newMem is the replacement char. Probs should check for already being in party
        self.partylist[slot] = newMem
    def statquery(self, num): #may or may not be useful
        form = '{stat:8} {val:8}'
        print form.format(stat = 'LEVEL', val = self.partylist[num].level)
        print form.format(stat = 'XP', val = self.partylist[num].xp)
        print form.format(stat = 'VIT', val = self.partylist[num].vit)
        print form.format(stat = 'STR', val = self.partylist[num].STR)
        print form.format(stat = 'INT', val = self.partylist[num].INT)
        print form.format(stat = 'DEF', val = self.partylist[num].DEF)
        print form.format(stat = 'STAMINA', val = self.partylist[num].stam)
        print form.format(stat = 'SPD', val = self.partylist[num].spd)
        #print form.format(stat = 'STUN', val = self.partylist[num]stun)
        #print form.format(stat = 'DRAIN', val = self.partylist[num]drain)
        #print form.format(stat = 'BIND', val = self.partylist[num]bind)
        #print form.format(stat = 'MUTE', val = self.partylist[num]mute)
