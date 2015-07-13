class spell(object):
    def __init__(self, typ, aoe):
      self.typ = typ #either phys, which is reduced by def + str, magic, reduced by def + int, pure, no reductions, or a non-damage
      #TODO
      #We need to feed it the list of spells joe has. It's going to suck. Just a lot of variety in here.

class unit(object):
    spell spellList[4]
    def __init__(self, name, level, xp, vit, STR, INT, DEF, stam, spd, stun, drain, bind, mute):
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

class party(object):
	unit partylist[4]
    def __init__(self, A, B, C, D) #create a party and assign to it
	self.partylist[0] = A
	self.partylist[1] = B
	self.partylist[2] = C
	self.partylist[3] = D
    def memSwap(self, slot, newMem) #slot is the position to change, newMem is the replacement char
        self.partylist[slot] = newMem
    def statquery(targetUnit): #may or may not be useful
        form = '{stat:8} {val:8}'
        name = raw_input ("Enter name of unit: ")
        print form.format(stat = 'LEVEL', val = targetUnit.level)
        print form.format(stat = 'XP', val = targetUnit.xp)
        print form.format(stat = 'VIT', val = targetUnit.vit)
        print form.format(stat = 'STR', val = targetUnit.STR)
        print form.format(stat = 'INT', val = targetUnit.INT)
        print form.format(stat = 'DEF', val = targetUnit.DEF)
        print form.format(stat = 'STAMINA', val = targetUnit.stam)
        print form.format(stat = 'SPD', val = targetUnit.spd)
        print form.format(stat = 'STUN', val = targetUnit.stun)
        print form.format(stat = 'DRAIN', val = targetUnit.drain)
        print form.format(stat = 'BIND', val = targetUnit.bind)
        print form.format(stat = 'MUTE', val = targetUnit.mute)
