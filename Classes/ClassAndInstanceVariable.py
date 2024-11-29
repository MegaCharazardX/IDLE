class Animal :
    dis = "Animal" #class variable
    _sa = ""
    def  __init__(self, _name, _animal, _kind = "Feline"):
        self.name = _name
        self.kind = _kind
        self.animal = _animal
        self.tricks = list()
        self._sa = _name
        #sa = _name
        
    def read(self):
        return self.sa

    def animalSpec(self):
        return f"{self.name} is a {self.animal} of {self.kind} family cpable of doing {self.tricks} tricks."

    def addTricks(self, _tricks):
        self.tricks.append(_tricks)

class Dog(Animal):

    def trial(self):
        print("Hello " + self.name + "\nKnown tricks :", self.tricks)
    
        
A = Animal("Rodger", "Dog", "Canine")
B = Animal("Shiloh", "Dog", "Canine")
C = Animal("Whiskers", "Cat")
D = Animal("Puss", "Cat")
A.addTricks("Stand, Play-Dead")
B.addTricks("Sit, Stay")
C.addTricks("Imitate, Play-Dead")
D.addTricks("Sleep, Slay")
print(A.animalSpec())
print(B.animalSpec())
print(C.animalSpec())
print(D.animalSpec())

D = Dog("Rodger", "Dog", "Canine")
D.addTricks("Stand, Play-Dead")
D.trial()
print(D._sa)
        




        
