class Dominic(unit):
    charge
    def __init__(self):
        #self, name, level, xp, VIT, STR, INT, DEF, STAM, SPD, VITup, STRup, INTup, DEFup
        super(Dominic, self).__init__(self, "Dominic", 1, 0, 90, 5, 5, 5, 10, 4, 10, 2, 2, 2)
        self.charge = 1
    def focus(self):
        charge += 1
    def gattle(enemyParty, pos):
        if (pos == 1):
             enemyParty[0].HP -= 50*charge
             enemyParty[1].HP -= 30*charge
             enemyParty[2].HP -= 30*charge
             enemyParty[3].HP -= 30*charge
        else if (pos == 2):
             enemyParty[1].HP -= 50*charge
             enemyParty[2].HP -= 30*charge
             enemyParty[3].HP -= 30*charge
        else
             print "How did this happen to me???? Dom gattle"
        charge = 1
    def chen(self, userParty):
        for p in userParty:
            p.HP += (50 + self.STR + self.INT)
            if (p.HP > p.VIT):
                p.HP = p.VIT
        self.drainD = 3
         





    
