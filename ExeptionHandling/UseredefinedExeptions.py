class ageOutBoundError:    
    def __init__(self, _age, _upperboundAge):
        raise Exception(f"{_age} should be less than {_upperboundAge}")

class AgeChecking :
    def __init__(self, _age, _uperagelimit):
        self.age = _age
        self.uperagelimit = _uperagelimit

    def isnum(self):
        if self.age.isdigit() == False:
            raise ValueError(f"{self.age} is not an integer")
        else:
            print("The age ")

    def is_in_range(self):      
        if int(self.age) > int(self.uperagelimit) or int(self.age) < 0:
            raise ageOutBoundError(self.age, int(self.uperagelimit))

f = open("Config.txt")
filecontents = f.readline().split(",")
uperagelimit = filecontents[0].split(":")[1]
age = input("Enter Age : ")
a = AgeChecking(age,uperagelimit)
a.is_in_range()
    
