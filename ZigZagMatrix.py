#  1  2  3  4
#  8  7  6  5
#  9 10  11 12


class ZigZagMatrix:
    def __init__(self, order = 3):
        self.order = order
        self.Matrix = []
        self.Elements = []
        self.ZigZagMatrix = []
        self.__MatrixInit()
        #self.ZigZag()
        
    def __MatrixInit(self) -> None : 
        for i in range(self.order**2)       :
            self.Elements.append(i+1)
            
        count = 0
        for i in range(self.order):
            slice = self.Elements[count : self.order+count]
            self.Matrix.append(slice)
            count += self.order
            
        #print(self.Matrix, self.Elements)

    def ZigZag(self, ):
        iseven = True
        tempMatrix = []
        for i in self.Matrix:
            if iseven:
                #print(i)
                tempMatrix.append(i)
                iseven = False
                
            elif iseven != True:
                #print(i[::])
                tempMatrix.append(i[::])   
                iseven = True
        self.ZigZagMatrix = tempMatrix.copy()
        
        return self.ZigZagMatrix
        
    
for i in ZigZagMatrix(4).ZigZag():
    print(i)
    