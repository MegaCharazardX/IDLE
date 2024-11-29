"""rowlist = []
columnlist = []
rows = int(input("Enter the number of rows : "))
for i in range (0, rows):
    column = int(input("Enter the number of columns : "))
    for i in range (0, column):
        column_elements = int(input("Enter the element : "))
        columnlist.append(column_elements)     
print(columnlist)"""

matrix1 = tuple(input("Enter the order of the first matrix :"))
matrix2 = tuple(input("Enter the order of the second matrix :"))
if matrix1 == matrix2:
    print("HI")
else:
    print("BYE")
