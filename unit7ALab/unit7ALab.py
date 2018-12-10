class Pet():
    petType = "cage free pet"
    def __init__(self, vType, vName, vBreed):
        self.type = vType
        self.name = vName
        self.breed = vBreed
    def whatIsIt(self):
        return("You have a " + self.type + " named " + self.name + " who is a " + self.breed + ".")

class Cage():
    petType = "caged pet"
    def __init__(self, vType, vDanger):
        self.type = vType
        self.danger = vDanger
    def whatDanger(self):
        if self.danger == "T":
            return("You have a dangerous " + self.type + ".")
        if self.danger == "F":
            return ("You have a safe " + self.type + ".")

myPet1 = Pet("dog", "Remy", "golden retriever")
print(myPet1.name)
print(myPet1.petType)
print(myPet1.whatIsIt())
print()

myPet2 = Pet("cat", "bagheera", "panther")
print(myPet2.name)
print(myPet2.petType)
print(myPet2.whatIsIt())
print()

myCage1 = Cage("snake", "T")
print(myCage1.type)
print(myCage1.petType)
print(myCage1.whatDanger())
print()

myCage2 = Cage("rat", "F")
print(myCage2.type)
print(myCage2.petType)
print(myCage2.whatDanger())
print()
