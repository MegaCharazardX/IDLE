class Stack :
    def __init__(self):
        self.Stack = []
        
    def __str__(self):
        return str(self.Stack)
    
    def Push(self):
        self.__element = input("Enter The Element To Push :")
        self.Stack.append(self.__element)
        
    def PushMany(self, ListOfElements : list):
        self.__ListOfElements = ListOfElements
        self.Stack.extend(self.__ListOfElements)
        
    def Pop(self):
        if len(self.Stack) == 0 :
            raise ValueError("Cannot Pop From An Empty Stack.")
        else:
            self.Stack.pop()
            return self.Stack
        
stck = Stack()
stck.PushMany(["asdf", 5])
print(stck)
stck.Pop()
print(stck)