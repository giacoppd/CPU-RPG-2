class unit(object):
    def __init__(self, level, xp, vit, STR, INT, DEF, stam, spd, stun, drain, bind, mute):
        self.level = level
        self.xp = xp
        self.vit = vit
        self.STR = STR
        self.INT = INT
        self.DEF = DEF
        self.stam = stam
        self.spd = spd
        self.stun = stun
        self.drain = drain
        self.bind = bind
        self.mute = mute
       
dummy = unit(0,0,0,0,0,0,0,0,0,0,0,0)       
joe = unit(1,0,50,4,5,3,5,2,0,0,0,0)
matt = unit(1,0,75,6,7,5,5,4,0,0,0,0)
dominic = unit(1,0,90,5,5,5,5,4,0,0,0,0)
nick = unit(1,0,60,5,6,5,5,6,0,0,0,0)

target = 0

class spell(object):
    def __init__(self, owner, target, svit, sstr, sint, sdef, sstam, sspd, sstun, sdrain, sbind, smute):
        self.owner = owner
        self.target = target
        self.svit = svit
        self.sstr = sstr
        self.sint = sint
        self.sdef = sdef
        self.sstam = sstam
        self.sspd = sspd
        self.sstun = sstun
        self.sdrain = sdrain
        self.sbind = sbind
        self.smute = smute
              
DDOS = spell(matt, dummy, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0)
    
    
main = {
    'dummy' : dummy,
    'joe' : joe,
    'matt' : matt,
    'nick' : nick,
    'dominic' : dominic,
    }
    
spelllist = {
    'DDOS' : DDOS,
    }

def statquery():
    form = '{stat:8} {val:8}'
    name = raw_input ("Enter name of unit: ")
    print form.format(stat = 'LEVEL', val = main[name].level)
    print form.format(stat = 'XP', val = main[name].xp)
    print form.format(stat = 'VIT', val = main[name].vit)
    print form.format(stat = 'STR', val = main[name].STR)
    print form.format(stat = 'INT', val = main[name].INT)
    print form.format(stat = 'DEF', val = main[name].DEF)
    print form.format(stat = 'STAMINA', val = main[name].stam)
    print form.format(stat = 'SPD', val = main[name].spd)
    print form.format(stat = 'STUN', val = main[name].stun)
    print form.format(stat = 'DRAIN', val = main[name].drain)
    print form.format(stat = 'BIND', val = main[name].bind)
    print form.format(stat = 'MUTE', val = main[name].mute)
    
def usespell():
    spellselect = raw_input ("Select spell ")
    target = raw_input ("Select target: ")
    main[target].svit -= spelllist[spellselect].svit
    main[target].sstr -= spelllist[spellselect].sstr
    main[target].sint -= spelllist[spellselect].sint
    main[target].sdef -= spelllist[spellselect].sdef
    main[target].sstam -= spelllist[spellselect].sstam
    main[target].sspd -= spelllist[spellselect].sspd
    main[target].sstun -= spelllist[spellselect].sstun
    main[target].sdrain -= spelllist[spellselect].sdrain
    main[target].sbind -= spelllist[spellselect].sbind
    main[target].smute -= spelllist[spellselect].smute
    statquery()

usespell()