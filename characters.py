from cpurpg import *
#TODO Bad positional input return false shit
#jenny C emboss?
#buffsss??????????? return trigger variable to party to apply buff
class Dom(unit):

    def __init__(self):
        #self, name, level, xp, VIT, STR, INT, DEF, STAM, SPD, VITup, STRup, INTup, DEFup
        super(Dom, self).__init__(self, "Dominic", 1, 0, 90, 5, 5, 5, 10, 4, 10, 2, 2, 2)    
        self.charge1 = 0
        self.charge2 = 0
    def debuffdown():
        self.stunPurge()
	super(Dom, self).debuffdown()
	if (self.charge1 > 0):
            self.charge1 -= 1
	if (self.charge2 > 0):
            self.charge2 -= 1

    def stunPurge(self):
        self.stunD = 0
    
    def focus(self):
        if (super(Dom, self).checkMute() == True):
            return False
        if (self.charge1 == 0):
            charge1 += 3
        elif ((self.charge2 == 0) and (self.charge1 == 2)):
            charge2 += 3
        elif ((self.charge2 == 2) and (self.charge1 == 1)):
            print "why you do this, you only get 2 stacks foo"
            return False
        else:
            print "how u do this"
            return False

    def gattle(enemyParty, pos):
        if (super(Dom, self).checkBind() == True):
            return False
        if(super(Dom, self).useSTAM(8) == False):
            return False
        if (self.charge1 == 0):
            amt = 1
        elif ((self.charge2 == 0) and (self.charge1 == 2)):
            amt = 2
        elif ((self.charge2 == 2) and (self.charge1 == 1)):
            amt = 3
        if (pos == 1):
            enemyParty[0].HP -= 50*amt
            enemyParty[1].HP -= 30*amt
            enemyParty[2].HP -= 30*amt
            enemyParty[3].HP -= 30*amt
        elif (pos == 2):
            enemyParty[1].HP -= 50*amt
            enemyParty[2].HP -= 30*amt
            enemyParty[3].HP -= 30*amt
        else:
             print "How did this happen to me???? Dom gattle"
             return False
        charge1 = 0
        charge2 = 0

    def chen(self, userParty):
        if (super(Dom, self).checkMute() == True):
            return False
        if(super(Dom, self).useSTAM(10) == False):
            return False
        for p in userParty:
            p.heal(50 + self.STR + self.INT)
        self.drainD = 3
        

class Yong(unit):
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Yong, self).__init__(self, "Yongwoon", 1, 0, 150, 10, 6, 0, 10, 5, 30, 3, 1, 0)
    
    def graniteKick(target):
        if (super(Yong, self).checkBind() == True):
            return False
        if(super(Yong, self).useSTAM(10) == False):
            return False
        target.HP -= (5*self.STR - target.DEF - target.STR)

    def bloodTrans(partyList):
        if (super(Yong, self).checkMute() == True):
            return False
        if(super(Yong, self).useSTAM(13) == False):
            return False
        for p in partyList:
            p.gainSTAM(3)
    
    def bodyTrans(target):
        if (super(Yong, self).checkMute() == True):
            return False
        if(super(Yong, self).useSTAM(5) == False):
            return False
        self.HP -= 50
        target.heal(5*self.STR)

class Haley(unit): 
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Haley, self).__init__(self, "Haley", 1, 0, 55, 5, 7, 9, 10, 5, 10, 1, 1, 2)
    
    def drainPurge(self):
        self.drainD = 0
    
    def unravel(self):
        if (super(Haley, self).checkMute() == True):
            return False
        if(super(Haley, self).useSTAM(3) == False):
            return False
        self.bindD = 0
    
    def dash(self, enemyParty):
        if (super(Haley, self).checkBind() == True):
            return False
        if(super(Haley, self).useSTAM(5) == False):
            return False
        for e in enemyParty:
             e.HP -= (2*self.STR + 10 - e.DEF - e.STR)        
    def mountainChisel(self, target):
        if (super(Haley, self).checkBind() == True):
            return False
        if(super(Haley, self).useSTAM(10) == False):
            return False
        target.HP -= (4*(3*self.STR + 15) - target.DEF)
    
    def whirlKick(self, enemyParty):
        if (super(Haley, self).checkBind() == True):
            return False
        if(super(Haley, self).useSTAM(3) == False):
            return False
        enemyParty[0].HP -= (2*self.STR + 15 - enemyParty[0].DEF - enemyParty[0].STR)    
        enemyParty[1].HP -= (2*self.STR + 15 - enemyParty[1].DEF - enemyParty[1].STR)    

class Nick(unit):
   
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Nick, self).__init__(self, "Nick", 1, 0, 60, 5, 6, 5, 10, 6, 10, 1, 1, 1)
    
    def takeaction(self, i): #nick has double move, is self even needed idk I wish I could compile
        super(Nick, self).takeaction(i)
        #TODO reprompt for input here
        #i = input()
        super(Nick, self).takeaction(i)
    
    def blitz(self, target):
        if (super(Nick, self).checkBind() == True):
            return False
        if(super(Nick, self).useSTAM(4) == False):
            return False
        target.HP -= ((self.STR + 30) - target.DEF - target.STR)
    
    def rally(self, target):
        if (super(Nick, self).checkMute() == True):
            return False
        if(super(Nick, self).useSTAM(4) == False):
            return False
        target.gainSTAM(4)
    
    def stretch(self):
        if(super(Nick, self).useSTAM(10) == False):
            return False
        self.stunD = 0
        self.bindD = 0
        self.drainD = 0
        self.muteD = 0

class Kath(unit):

    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Kath, self).__init__(self, "Katherine", 1, 0, 70, 7, 7, 7, 10, 4, 10, 2, 2, 2)
        self.fort = False

    def totem(self, enemyParty):
        if (super(Kath, self).useSTAM(10) == False):
            return False
        for e in enemyParty:
            e.stunD = 2
        self.stunD += 2
        self.drainD += 2

    def obliteration(self, enemyParty):
        if (super(Kath, self).checkMute() == True):
            return False
        if (super(Kath, self).useSTAM(10) == False):
            return False
        DMG = (self.HP // 2) #damage is floored with the //
        for e in enemyParty:
            e.HP -= DMG
        self.HP -= DMG
    
    def uniPurge(self, userParty):
        if (super(Kath, self).checkMute() == True):
            return False
        if (super(Kath, self).useSTAM(10) == False):
            return False
        for u in userParty:
            u.stunD = 0
            u.bindD = 0
            u.muteD = 0
            u.drainD = 0
        self.drainD = 9999
        self.stunD = 9999 #big numbers so she's down for the count
   
    def fortressT(self): #TODO toggle takes 1 turn and no stam
        if (super(Kath, self).useSTAM(6) == False):
            return False
        if(self.fort == False):
           self.fort == True
           self.bindD = 9999
           self.DEF = (self.DEF*2)
        elif(self.fort == True):
           self.fort == False
           self.DEF = (self.DEF / 2)

class JennyK(unit):

    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(JennyK, self).__init__(self, "Jenny Kim", 1, 0, 85, 7, 6, 6, 10, 3, 10, 2, 2, 1)
        self.block = False
    
    def block(self):
        if (super(JennyK, self).checkBind() == True):
            return False
        if(super(JennyK, self).useSTAM(3) == False):
            return False
        self.block = True
    
    def piercingKick(self, target):
        if (super(JennyK, self).checkBind() == True):
            return False
        if (super(JennyK, self).useSTAM(4) == False):
            return False
        target.HP -= ((2*self.STR + 2*self.INT) - target.DEF - target.STR) #Row reduction?

    def ROTCDrill(self, tiarget):
        if (super(JennyK, self).checkBind() == True):
            return False
        if (super(JennyK, self).useSTAM(5) == False):
            return False
        target.gainSTAM(5)
    
    def artOfDeath(self, target):
        if (super(JennyK, self).checkMute() == True):
            return False
        if (super(JennyK, self).useSTAM(10) == False):
            return False
        target.HP -= (target.VIT - target.HP)

class JennyC(unit):
    
    embossD = 0
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(JennyC, self).__init__(self, "Jenny Chang", 1, 0, 60, 5, 6, 7, 10, 5, 10, 1, 2, 1)
        self.embossD = 0
    
    def debuffdown():
	super(JennyC, self).debuffdown()
	if (embossD > 0):
	    embossD -= 1
	    if(embossD == 0):
		return "emOFF"
	
    def vitalize(self, userParty):
        if (super(JennyC, self).checkMute() == True):
            return False
        if (super(JennyC, self).useSTAM(2) == False):
            return False
        for u in userParty:
            u.heal(self.INT + 5)

    def invigorate(self, userParty):
        if (super(JennyC, self).checkMute() == True):
            return False
        if (super(JennyC, self).useSTAM(3) == False):
            return False
        for u in userParty:
            u.gainSTAM(1)

    def remove(self, target, choice):
        if (super(JennyC, self).checkMute() == True):
            return False
        if (super(JennyC, self).useSTAM(7) == False):
            return False
        if(choice == 1):
            target.stunD = 0
        if(choice == 2):
            target.drainD = 0
        if(choice == 3):
            target.muteD = 0
        if(choice == 4):
            target.bindD = 0
        else:
            print "How did this happen to me? jennyC remove"
            return False

    def emboss(self, userParty): 
        if (super(JennyC, self).checkMute() == True):
            return False
        if (super(JennyC, self).useSTAM(10) == False):
            return False
        for u in userParty:
            User.embossAmount = self.DEF #accessing the static variable in Unit
            u.DEF += User.embossAmount
            u.embossD = 2


class Natasha(unit):
   
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Natasha, self).__init__(self, "Natasha", 1, 0, 105, 8, 5, 6, 10, 3, 20, 3, 2, 1)
        self.qD = 0
        self.qStack = 0
    
    def debuffdown():
	super(Natasha, self).debuffdown()
	if (qD > 0):
	    qD -= 1
	    if(qD == 0):
		self.DEF -= self.qStack*2
                self.qStack = 0
    
    def qigong(self):
        if (super(Natasha, self).checkBind() == True):
            return False
        if(super(Natasha, self).useSTAM(3) == False):
            return False
        self.DEF += 2
        self.qStack += 1
        self.qD += 3

    def unrefinedKick(self, target):
        if (super(Natasha, self).checkBind() == True):
            return False
        if (super(Natasha, self).useSTAM(3) == False):
            return False
        amount = ((3*self.STR + 10) - target.DEF - target.STR) 
        target.HP -= amount
        self.HP -= amount // 2

    def gungirFlourish(self, target):
        if (super(Natasha, self).checkBind() == True):
            return False
        if(super(Natasha, self).useSTAM(8) == False):
            return False
        target.HP -= ((8*(2*self.STR + 10 - target.DEF - target.STR)))
    
    def gungirCombo(self, target):
        if (super(Natasha, self).checkBind() == True):
            return False
        if(super(Natasha, self).useSTAM(10) == False):
            return False
        target.HP -= (8*((2*self.STR + 10) - (target.DEF + target.STR)))

class Ulri(unit):
   
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Ulri, self).__init__(self, "Ulri", 1, 0, 75, 6, 6, 5, 10, 3, 10, 2, 2, 3)
        self.phD = 0 #phalanx duration
    
    def debuffdown():
	super(Ulri, self).debuffdown()
	if (phD > 0):
	    phD -= 1
	    if(phD == 0):
	        self.DEF -= DEF
			
    def trueStrike(self, target):
        if (super(Ulri, self).checkBind() == True):
            return False
        if(super(Ulri, self).useSTAM(5) == False):
            return False
        target.HP -= (2*(self.STR + self.INT) - target.STR)

    def phalanx(self, target): 
        if (super(Ulri, self).checkBind() == True):
            return False
        if(super(Ulri, self).useSTAM(5) == False):
            return False
        target.bindD = 4
        self.DEF += 10
        self.phD = 4
        
    def oblation(self, userParty):   
        if(super(Ulri, self).useSTAM(10) == False):
            return False
        if (super(Ulri, self).checkMute() == True):
            return False
        for u in userParty:
            u.gainSTAM(10)
        self.HP -= (self.VIT * .7) // 1 #cheater's floor func, why import when you can just //?

class Morgan(unit):
   
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Morgan, self).__init__(self, "Morgan", 1, 0, 70, 7, 7, 5, 10, 3, 10, 1, 2, 1)
        self.duo = False
    
    def duoCheck(self, userParty):
        self.duo = False
        for u in userParty:
            if(u.name == "Rachel"):
                self.duo = True
                self.SPD += 2
                #Bind immune?
    
    def danceKnives(self, target):
        if (super(Morgan, self).checkBind() == True):
            return False
        if (super(Morgan, self).useSTAM(5) == False):
           target.HP -= (5*(self.STR + 10) - target.DEF)
    
    def danceDazzle(self, enemyParty):
        if (super(Morgan, self).checkBind() == True):
            return False
        if (super(Morgan, self).useSTAM(5) == False):
            return False
        for e in enemyParty:
            e.HP -= 40
        enemyParty[0].stunD = 1

    def danceDeath(self, enemyParty, userParty, roster):
        if (super(Morgan, self).checkBind() == True):
            return False
        if (self.duo == False):
            return False
        if (super(Morgan, self).useSTAM(10) == False):
            return False
        for e in enemyParty:
            e.HP -= (3*self.STR + 50) - (e.DEF + e.STR)
        


class Rachel(unit):
   
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Rachel, self).__init__(self, "Rachel", 1, 0, 80, 8, 7, 3, 10, 4, 15, 2, 2, 2)
        #TODO finish these stupid sisters when I have proper swaping


class Chris(unit):
   
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Chris, self).__init__(self, "Christine", 1, 0, 70, 6, 8, 6, 10, 3, 5, 1, 2, 1)
    
    def analyze(self, target):
        if (super(Chris, self).useSTAM(5) == False):
            return False
        if (super(Chris, self).checkMute() == True):
            return False
        target.analyzeB = True

    def cripple(self, target):
        if (super(Chris, self).useSTAM(8) == False):
            return False
        if (super(Chris, self).checkMute() == True):
            return False
        target.HP -= (4*self.INT + 20 - target.DEF - target.INT)
        target.bindD = 2
        target.muteD = 2

    def deepPurge(self, userParty):
        if (super(Chris, self).useSTAM(8) == False):
            return False
        for u in userParty:
            u.muteD = 0
        
class Matt(unit):

    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Matt, self).__init__(self, "Matt", 1, 0, 75, 6, 7, 5, 10, 4, 10, 1, 2, 2)
        self.YOLOD = 0#yolo duration
        self.it = 0 #Iteration toggle

    def debuffdown(self):
	super(Matt, self).debuffdown()
	if (self.YOLOD > 0):
	    YOLOD -= 1
	    if(YOLOD == 0):
		self.DEF -= 5
                self.STR -= 5
                self.INT -= 5

    def debugg(self, target):
        if (super(Matt, self).useSTAM(5) == False):
            return False
        if (super(Matt, self).checkMute() == True):
            return False
        target.bindD = 0
        target.muteD = 0
        target.drainD = 0
        if (self.it == 1):
            target.stunD = 0
            self.it = 0

    def YOLO(self):
        if (super(Matt, self).useSTAM(10) == False):
            return False
        if (super(Matt, self).checkMute() == True):
            return False
        self.YOLOD = 5
        self.STR += 5 
        self.INT += 5
        self.DEF += 5
    
    def iter(self):
        if (super(Matt, self).useSTAM(3) == False):
            return False
        if (super(Matt, self).checkMute() == True):
            return False
        self.it = 1
        #TODO Raw input stuff here
    
    def DDOS(self, target): 
        if (super(Matt, self).useSTAM(5) == False):
            return False
        if (super(Matt, self).checkMute() == True):
            return False
        target.HP -= (3*self.INT) - (target.DEF + target.INT)
        if (self.it == 1):
            target.stunD = 3
            self.it = 0
        else:
            target.stunD = 1
        
class Joe(unit):
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Joe, self).__init__(self, "Joe", 1, 0, 50, 4, 5, 3, 10, 2, 5, 1, 2, 1)
    
    def melancholy(self, enemyParty):
        if (super(Joe, self).useSTAM(4) == False):
            return False
        if (super(Joe, self).checkMute() == True):
            return False
        for e in enemyParty:
            e.STAM -= 3
            if (e.STAM < 0):
                e.STAM = 0

    def exhaust(self, target):
        if (super(Joe, self).useSTAM(4) == False):
            return False
        if (super(Joe, self).checkMute() == True):
            return False
        target.drainD = 3

    def chaos(self, enemyParty):
        if (super(Joe, self).useSTAM(6) == False):
            return False
        if (super(Joe, self).checkMute() == True):
            return False
        for e in enemyParty:
            e.HP -= (3*self.INT + 20) - (e.INT + e.DEF)
        self.stunD = 1

    def bloodFlare(self, target):
        if (super(Joe, self).useSTAM(4) == False):
            return False
        if (super(Joe, self).checkMute() == True):
            return False
        self.HP /= 2
        target.HP -= (10*self.INT)


class Galen(unit):
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Galen, self).__init__(self, "Galen", 1, 0, 90, 8, 4, 4, 10, 4, 5, 1, 3, 1)
    
    def bash(self, target):
        if (super(Galen, self).useSTAM(8) == False):
            return False
        if (super(Galen, self).checkBind() == True):
            return False
        target.HP -= (2*self.STR - (target.DEF + target.STR))
        target.stunD = 2

    def serve(self, target): 
        if (super(Galen, self).useSTAM(4) == False):
            return False
        if (super(Galen, self).checkBind() == True):
            return False
        target.HP -= (self.INT + self.STR - (target.DEF + target.STR))
        target.bindD = 2
    
    def wellVersed(self, target):
        if (super(Galen, self).useSTAM(8) == False):
            return False
        if (super(Galen, self).checkMute() == True):
            return False
        target.HP -= (2*self.INT - (target.DEF + target.INT))
        target.muteD = 3
    
    def prep(self):
        if (super(Galen, self).useSTAM(5) == False):
            return False
        if (super(Galen, self).checkMute() == True):
            return False
        self.DEF += self.INT
        prepD = 1

    def prepOFF(self): #turns prep off. not sure how to make it an option...
        prepD = 0
        self.DEF -= self.INT
    
    def debuffdown(self):
	super(Galen, self).debuffdown()
	if (self.prepD > 0):
            if (super(Galen, self).useSTAM(2) == False):
                prepD = 0
                self.DEF -= self.INT


class James(unit):
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(James, self).__init__("James", 1, 0, 100, 7, 5, 6, 10, 3, 15, 3, 1, 2)
    
    def greatPurge(self, target):
        if (super(James, self).useSTAM(6) == False):
            return False
        target.bindD = 0
        target.muteD = 0
        target.drainD = 0
    
    def lessPurge(self, target):
        if (super(James, self).useSTAM(3) == False):
            return False
        target.drainD = 0

    def cleanse(self, target):
        if (super(James, self).useSTAM(4) == False):
            return False
        if (super(James, self).checkMute() == True):
            return False
        target.heal(self.STR + 20)

    def sacrifice(self, target):
        if (super(James, self).useSTAM(10) == False):
            return False
        if(target.HP != 0):
            return False
        else:
            target.HP = target.VIT
            target.STAM = 10
            target.bindD = 0
            target.muteD = 0
            target.stunD = 0
            target.drainD = 0
            self.HP = 0

class Ashwin(unit):
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Ashwin, self).__init__(self, "Ashwin", 1, 0, 80, 6, 8, 6, 10, 3, 10, 2, 2, 1)
        self.imfD = 0 #Duration of buff immaculateForm

    def debuffdown():
        super(Ashwin, self).debuffdown()
        if (imfD > 0):
            imfD -= 1
            if(imfD == 0):
                self.STR -= self.STR // 3 #Example: 5 + 2.5 = 7 --> 7 - 7/3 = 5
                self.INT -= self.INT // 3

    def smash(self, target):
        if (super(Ashwin, self).useSTAM(7) == False):
            return False
        if (super(Ashwin, self).checkBind() == True):
            return False
        target.HP -= (5*self.STR - target.DEF - target.STR)
            
    def logicBlast(self, target):
        if (super(Ashwin, self).useSTAM(7) == False):
            return False
        if (super(Ashwin, self).checkMute() == True):
            return False
        target.HP -= (5*self.STR - target.DEF - target.INT)
        
    def immaculateForm(self):
        if (super(Ashwin, self).useSTAM(10) == False):
            return False
        if (super(Ashwin, self).checkMute() == True):
            return False
        if (self.imfD == 0):
            self.STR += self.STR // 2 #rounded down
            self.INT += self.INT // 2 #rounded down
            self.imfD += 4
        elif self.imfD > 0:
            self.imfD == 4
    
class Kenji(unit):
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Kenji, self).__init__(self, "Kenji", 1, 0, 80, 8, 8, 4, 10, 4, 15, 2, 2, 1)
    
    def barrier(self, target):
        if (super(Kenji, self).useSTAM(5) == False):
            return False
        if (super(Kenji, self).checkMute() == True):
            return False
        target.DEF += 5
        target.barrD = 4

    def CAD(self, enemyParty):                
        if (super(Kenji, self).useSTAM(8) == False):
            return False
        if (super(Kenji, self).checkMute() == True):
            return False
        for e in enemyParty:
            e.bindD = 3

    def VocalBoom(self, enemyParty):                
        if (super(Kenji, self).useSTAM(8) == False):
            return False
        if (super(Kenji, self).checkMute() == True):
            return False
        for e in enemyParty:
            e.muteD = 3
    
    def friendship(self, userParty):
        #TODO Triple swap shit
        print("emmes")
