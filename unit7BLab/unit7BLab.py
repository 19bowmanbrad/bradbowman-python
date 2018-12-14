class Pet():
    def __init__(self, vName, vBreed):
        self.name = vName
        self.breed = vBreed
    def info(self):
        return(self.name + " is a " + self.breed)

class Dog(Pet):
    def __init__(self, vName, vBreed, vActivity):
        Pet.__init__(self, vName, vBreed)
        self.activity = vActivity
    def description(self):
        return(self.info() + " that likes to " + self.activity)




def main():
    myPet1 = Pet("Remy", "golden retriever")
    print(myPet1.info() + ".")
    myPet2 = Dog("Remy", "golden retriever", "sleep")
    print(myPet2.description() + ".")

main()
