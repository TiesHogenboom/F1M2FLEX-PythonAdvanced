class Vriend :

    levens = 10
    level = "level 1"
    snelheid = 5.5
    levend = True

    def Print(self) :
        print("Test 1")

    def ExtraLevens(self) : 
        self.levens += 10
        print("Je hebt nu", self.levens, "levens!")


    
class Vijand (Vriend) :
    Anger = 100
    Enemy = True

    def __init__(self) :
        self.snelheid += 2.2
        print("Je snelheid gaat met 2.2 omhoog! Je snelheid is nu :", self.snelheid)

        self.levend = False
        print("Ben je levend?", self.levend, "!")
    
    def Print(self):
        print("Test 2")

    def ExtraLevens(self) :
        super().__init__()
        self.levens = 50
        print("Je hebt", self.levens, "levens")


classVriend = Vriend()
classVijand = Vijand()




classVriend.ExtraLevens()
classVriend.Print()



print("-------------------------------------")
classVijand.__init__()
classVijand.Print()
classVijand.ExtraLevens()
print("-------------------------------------")
classVriend.ExtraLevens()