from prettytable import PrettyTable
import string

class Matrix:
    def __init__(self, order: str) -> None:
        self.table = PrettyTable()
        self.table.border = False
        self.table.header = False
        self.table.align = "c"
        self.order = order
        self.matrix: list = []
        self.numberOfRows: int = 0
        self.numberOfColumn: int = 0
        self.numberOfElement: int = self.numberOfRows * self.numberOfColumn
        self.__evalOrder()

    def __str__(self):
        return str(self.table)

    def __evalOrder(self):
        self.__exeptx = string.ascii_letters.replace("x", "")
        for char in self.__exeptx:
            if char in self.order:
                raise ValueError(f"Invalid Order: {self.order}")
        if self.order.count("x") > 1:
            raise ValueError("Invalid Order")
        if "x" not in self.order:
            self.numberOfRows, self.numberOfColumn = int(self.order)
        else:
            self.__orderList = self.order.split("x")
            self.numberOfRows, self.numberOfColumn = int(self.__orderList[0]), int(self.__orderList[-1])

    def InitMatrix(self, matrix=[], matrixReturn=True, matrixPrint=False):
        if matrix == []:
            for i in range(self.numberOfRows):
                self.__row = input(f"Enter the row number {i + 1} (Elements separated by ,) : ").split(",")
                if len(self.__row) != self.numberOfColumn:
                    raise ValueError(f"Element Defies The Order of {self.order}")
                else:
                    self.matrix.append([int(x) for x in self.__row])
            for __row in self.matrix:
                self.table.add_row(__row)  # Add rows to PrettyTable for printing
            if matrixPrint:
                print(self.table)
            if matrixReturn:
                return self.table
        else:
            self.matrix = [i for i in matrix]
            for i in self.matrix:
                if len(i) != self.numberOfColumn:
                    raise ValueError(f"Element Defies The Order of {self.order}")
            for __row in self.matrix:
                self.table.add_row(__row)  # Add rows to PrettyTable for printing
            if matrixPrint:
                print(self.table)
            if matrixReturn:
                return self.table

    def Transpose(self):
        if not self.matrix:
            raise ValueError("Matrix Not Initialized")
        else:
            transposedTableData = list(zip(*self.matrix))  # Use self.matrix for transposing
            self.temp_table = PrettyTable()
            self.temp_table.border = False
            self.temp_table.header = False
            self.temp_table.align = "c"
            for i in transposedTableData:
                self.temp_table.add_row(i)
            return self.temp_table

    def Multiply(self, other=1):
        if isinstance(other, (int, float)):
            print(f"Scalar multiplication by {other}")
            if other != 1:
                tempmatrix = []
                for i in self.matrix:
                    multipliedRow = [other * x for x in i]
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
            # Ensure that the matrices can be multiplied
            if self.numberOfColumn != other.numberOfRows:
                raise ValueError(f"Cannot multiply: {self.numberOfColumn} columns in A != {other.numberOfRows} rows in B.")

            # Initialize the result matrix
            result_matrix = [[0 for _ in range(other.numberOfColumn)] for _ in range(self.numberOfRows)]

            # Perform matrix multiplication
            for i in range(self.numberOfRows):
                for j in range(other.numberOfColumn):
                    for k in range(self.numberOfColumn):
                        result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

            # Create PrettyTable for result matrix
            result_table = PrettyTable()
            result_table.border = False
            result_table.header = False
            result_table.align = "c"
            for row in result_matrix:
                result_table.add_row(row)

            return result_table
        else:
            raise TypeError("Unsupported type for multiplication")

    def Add(self, other):
        if isinstance(other, Matrix):
            print(f"Adding matrix of order {other.order} to the current matrix")
            # Ensure that the matrices have the same dimensions
            if self.numberOfRows != other.numberOfRows or self.numberOfColumn != other.numberOfColumn:
                raise ValueError(f"Cannot add: Matrices have different dimensions ({self.numberOfRows}x{self.numberOfColumn} vs {other.numberOfRows}x{other.numberOfColumn}).")

            # Perform matrix addition
            result_matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.numberOfColumn)] for i in range(self.numberOfRows)]

            # Create PrettyTable for result matrix
            result_table = PrettyTable()
            result_table.border = False
            result_table.header = False
            result_table.align = "c"
            for row in result_matrix:
                result_table.add_row(row)

            return result_table
        
        elif isinstance(other, (int, float)):
            print(f"Scalar addition of {other} to the current matrix")
            # Perform scalar addition
            result_matrix = [[self.matrix[i][j] + other for j in range(self.numberOfColumn)] for i in range(self.numberOfRows)]

            # Create PrettyTable for result matrix
            result_table = PrettyTable()
            result_table.border = False
            result_table.header = False
            result_table.align = "c"
            for row in result_matrix:
                result_table.add_row(row)

            return result_table

        else:
            raise TypeError("Unsupported type for addition")

    def Subtract(self, other):
        if isinstance(other, Matrix):
            print(f"Subtracting matrix of order {other.order} from the current matrix")
            # Ensure that the matrices have the same dimensions
            if self.numberOfRows != other.numberOfRows or self.numberOfColumn != other.numberOfColumn:
                raise ValueError(f"Cannot subtract: Matrices have different dimensions ({self.numberOfRows}x{self.numberOfColumn} vs {other.numberOfRows}x{other.numberOfColumn}).")

            # Perform matrix subtraction
            result_matrix = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.numberOfColumn)] for i in range(self.numberOfRows)]

            # Create PrettyTable for result matrix
            result_table = PrettyTable()
            result_table.border = False
            result_table.header = False
            result_table.align = "c"
            for row in result_matrix:
                result_table.add_row(row)

            return result_table
        
        elif isinstance(other, (int, float)):
            print(f"Scalar subtraction of {other} from the current matrix")
            # Perform scalar subtraction
            result_matrix = [[self.matrix[i][j] - other for j in range(self.numberOfColumn)] for i in range(self.numberOfRows)]

            # Create PrettyTable for result matrix
            result_table = PrettyTable()
            result_table.border = False
            result_table.header = False
            result_table.align = "c"
            for row in result_matrix:
                result_table.add_row(row)

            return result_table

        else:
            raise TypeError("Unsupported type for subtraction")

# Test code
A = Matrix("2x2")
print(f"{A.numberOfRows}x{A.numberOfColumn}")
A.InitMatrix(matrix=[[1, 2], [2, 3]])
print(A)

B = Matrix("2x2")
print(f"{B.numberOfRows}x{B.numberOfColumn}")
B.InitMatrix(matrix=[[1, 2], [4, 8]])
print(B)

print("Subtracting B from A:")
print(A.Subtract(B))  # Matrix subtraction

print("Subtracting scalar 5 from A:")
print(A.Subtract(5))  # Scalar subtraction

# Test code
A = Matrix("2x2")
print(f"{A.numberOfRows}x{A.numberOfColumn}")
A.InitMatrix(matrix=[[1, 2], [2, 3]])
print(A)

B = Matrix("2x2")
print(f"{B.numberOfRows}x{B.numberOfColumn}")
B.InitMatrix(matrix=[[1, 2], [4, 8]])
print(B)

print("Adding A and B:")
print(A.Add(B))  # This should now add matrices A and B correctly.

print("Adding scalar 5 to A:")
print(A.Add(5))  # This should now add scalar 5 to matrix A correctly.


# Test code
A = Matrix("2x2")
print(f"{A.numberOfRows}x{A.numberOfColumn}")
A.InitMatrix(matrix=[[1, 2], [2, 3]])
print(A)

B = Matrix("2x2")
print(f"{B.numberOfRows}x{B.numberOfColumn}")
B.InitMatrix(matrix=[[1, 2], [4, 8]])
print(B)

print("Multiplying A and B:")
print(A.Add(B))  # This should now multiply matrices A and B correctly.
