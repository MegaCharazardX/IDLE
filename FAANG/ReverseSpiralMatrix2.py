from prettytable import PrettyTable
class ReverseSpiralMatrix:
    def __init__(self, x):
        self.table = PrettyTable()
        self.x = x 
        self.numOfElem = x**2
        self.ElemList = []
        self.Matrix = []
        self.table.border = False
        self.table.header = False
        self.table.align = "l"
    
    def __ElemListInit(self) -> None: 
        for element in range(self.numOfElem):
            self.ElemList.append(element+1)
        
    def __MatrixInit(self) -> None:
        self.__count = 0
        for i in range(self.x):
            _slice = self.ElemList[self.__count : self.x + self.__count]
            self.Matrix.append(_slice)
            self.__count += self.x
        
    def SpiralMatrix(self) -> PrettyTable: 
        self.__ElemListInit()
        self.__MatrixInit()
        for i in self.Matrix:
            self.table.add_row(i)
        print(type(self.table))    
        return self.table
    
    def ReverseSpiralMatrix(self):
        self.__ElemListInit()
        self.__MatrixInit()
        __Matrix = self.Matrix[::-1]
        for i in __Matrix:
            self.table.add_row(i)
        print(type(self.table))    
        return self.table
    
obj = ReverseSpiralMatrix(3)
print(obj.ReverseSpiralMatrix()) 
        