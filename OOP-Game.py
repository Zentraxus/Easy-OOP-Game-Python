class Rassen:
    def __init__(self, name, leben, beschr):
        self.name = name 
        self.leben = leben
        self.beschr = beschr
        
class Mensch(Rassen):
    def __init__(self):
        Rassen.__init__(self, "Mensch", 2, "intelligent - macht Elementarschaden mit einem Zauber")
    
class Monster(Rassen):
    def __init__(self):
        Rassen.__init__(self, "Monster", 2, "gefräßig - ständig auf der Suche nach frischem Fleisch")
        
    def schaden(self):
        self.leben = self.leben - 1 
        
    def beschreibung(self):
        if self.leben == 2:
            leben = "Das Monster ist gesund."
        elif self.leben == 1:
            leben = "Das Monster ist stark verletzt!"
        elif self.leben == 0:
            leben = "Das Monster ist tot."
        return self.name + " - " + self.beschr + "\n" + "(mit " + str(self.leben) + " Lebenspunkten)" 
        
Monster = Monster()        
        
def Beobachten(Substantiv):
    if Substantiv == "Monster":
        return Monster.beschreibung()
    elif Substantiv == "Mensch":
        return Mensch().beschr
    else:
        return print("Es gibt kein {}.".format(Substantiv))
        
def Angriff(Substantiv):
    if Substantiv == "Monster":
        Monster.schaden()
        print(Monster.leben)
        if Monster.leben <= 0:
            return "Du hast das Monster getötet."
        else:
            return "Das Monster hat einen Lebenspunkt verloren."
            
akzeptierte_verben = {
    "beobachte": Beobachten,
    "schlage": Angriff,
}

def Benutzereingabe():
    M = input(": ").split()
    Verb = M[0]
    if Verb in akzeptierte_verben:
        x = akzeptierte_verben[Verb]
    else: 
        print("Das macht Leben nur kompliziert.")
        return 
    
    if len(M) == 2:
        Substantiv = M[1]
        print(x(Substantiv))
    else:
        print("Was tust Du da?")
        
while True:
    Benutzereingabe()
