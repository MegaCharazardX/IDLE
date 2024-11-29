class Animal1:
    def __init__(self, _name):
        self.name = _name

    def animalFunc(self):
        return self.name
        
class AnimalBase :
    dis = "Animal" #class variable
    sa = ""
    def  __init__(self, _name, _animal, _kind = "Canine"):
        self.name = _name
        self.kind = _kind
        self.animal = _animal
        self.tricks = list()
        #self.__sa = __name
        self.a = "Mammal"
        self.sa = _name
        
    def read(self):
        return self.sa

    def animalSpec(self):
        return f"{self.name} is a {self.animal} of {self.kind} family cpable of doing {self.tricks} tricks."

    def addTricks(self, _tricks):
        self.tricks.append(_tricks)

class Mammal(AnimalBase):
    def printMammal(self):
        pass
    
#class Dog(Animal, Mammal):
class Dog(Mammal, Animal1):

    def trial(self):
        print(f"Hell0 {self.name} \n known tricks {self.tricks} \n You're a {self.a}")


b = Dog("a", "b")
b.addTricks("Sit, Stay")
print(b.animalFunc())
#print(b.read())
#b.trial()
    
        

        
