class addition :
    def __init__(self):
        self.lst = []


    def append (self,element):
        for i in range (0,3):
            self.lst.append(element)
            return self.lst









obj = addition()

elem = input("Enter the element :")
retlist = obj.append(elem)
print(retlist)
