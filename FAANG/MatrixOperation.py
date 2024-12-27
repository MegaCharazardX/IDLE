import string
from prettytable import PrettyTable


class Matrix:
    def __init__(self, order : str) -> None:
        self.table = PrettyTable()
        self.table.border = False
        self.table.header = False
        self.table.align = "c"
        self.order = order
        self.matrix : list = []
        self.numberOfRows: int = 0
        self.numberOfColumn: int = 0
        self.numberOfElement: int = self.numberOfRows * self.numberOfColumn
        self.__evalOrder()        
    
    def __str__(self):
        return self.table
    
    def __evalOrder(self):
        self.__exeptx = string.ascii_letters.replace("x", "")
        for char in  self.__exeptx :
            if char in self.order:
                raise ValueError(f"Invalid Order : {self.order}")
        if self.order.count("x") > 1:
            raise ValueError("Invalid Order")
        if "x" not in self.order : 
            self.numberOfRows, self.numberOfColumn = int(self.order)
        else :
            self.__orderList = self.order.split("x")
            self.numberOfRows, self.numberOfColumn = int(self.__orderList[0]), int(self.__orderList[-1])
            self.numberOfElement: int = self.numberOfRows * self.numberOfColumn
            
    def InitMatrix(self, matrix = [], matrixReturn = True, matrixPrint = False):
        if matrix == []:
            for i in range(self.numberOfRows):
                self.__row = input(f"Enter the row number {i+1} (Elements seperated by ,) : ").split(",")
                if len(self.__row) != self.numberOfColumn :
                    raise ValueError(f"Element Defies The Order of {self.order}")
                else:
                    self.matrix.append([int(x) for x in self.__row])
            for __row in  self.matrix:
                self.table.add_row(__row) #print(__row)
            if matrixPrint == True:
                print(self.table)
            if matrixReturn == True:
                return self.table
        else:
            self.matrix = [i for i in matrix]
            for i in self.matrix:
                if len(i) != self.numberOfColumn :
                    raise ValueError(f"Element Defies The Order of {self.order}")
            for __row in  self.matrix:
                self.table.add_row(__row) #print(__row)
            if matrixPrint == True:
                print(self.table)
            if matrixReturn == True:
                return self.table       
            
    def Transpose(self):
        if self.matrix == []:
            raise ValueError("Matrix Not Initailized")
        else:
            transposedTableData = list(zip(*self.table._rows))
            self.temp_table = PrettyTable()
            self.temp_table.border = False
            self.temp_table.header = False
            self.temp_table.align = "c"
            for i in transposedTableData:
                self.temp_table.add_row(i)
            return self.temp_table
        
    #def Multiply(self, scalar: int = 1 ):
        
    def Multiply(self, other=1):
        if isinstance(other, (int, float)):
            print(f"Scalar multiplication by {other}")
            if other !=1:
                tempmatrix = []
                for i in self.matrix:
                    multipliedRow = []
                    for j in i:
                        multipliedRow.append(other*j)
                    tempmatrix.append(multipliedRow)
                self.matrix = tempmatrix
                self.temp_table = PrettyTable()
                self.temp_table.border = False
                self.temp_table.header = False
                self.temp_table.align = "c"
                for i in tempmatrix:
                    self.temp_table.add_row(i)
                return self.temp_table
            else:
                return self.table
        elif isinstance(other, Matrix):
            print(f"Matrix multiplication with another matrix of order {other.order}")
            
            if self.numberOfColumn != other.numberOfRows:
                raise ValueError(f"Cannot multiply: {self.numberOfColumn} columns in A != {other.numberOfRows} rows in B.")

            # Resultant matrix dimensions: self.numberOfRows x other.numberOfColumn
            result_matrix = [[0 for _ in range(other.numberOfColumn)] for _ in range(self.numberOfRows)]

            # Perform multiplication
            for i in range(self.numberOfRows):
                for j in range(other.numberOfColumn):
                    for k in range(self.numberOfColumn):
                        result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

            # Convert result_matrix into a PrettyTable for display
            result_table = PrettyTable()
            result_table.border = False
            result_table.header = False
            result_table.align = "c"
            for row in result_matrix:
                result_table.add_row(row)

            return result_table
        else:
            raise TypeError("Unsupported type for multiplication")
        
    def Add(self, other = 0):
        tempMatrix = self.matrix
        if isinstance(other, (int, float)):
            for i in self.matrix:
                for j in i :
                    

            
A = Matrix("2x2")
print(f"{A.numberOfRows}x{A.numberOfColumn}")
print(A.InitMatrix(matrix=[[1,2], [2,3]]))
#print(A.Multiply(2))

B = Matrix("2x2")
print(f"{B.numberOfRows}x{B.numberOfColumn}")
print(B.InitMatrix(matrix=[[1,2], [4,8]]))
print(B.Multiply(2))
print(A.Multiply(B))
#ob NOHES.gg