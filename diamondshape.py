row =int(input("Enter the number of rows : "))
symb = input("Enter the symbol to print : ")
k = round(row/2)*2
for i in range (0, row):
    for j in range (0, k+1):
        print(end = " ")
    for j in range (0, i +1):
        print(symb,end = "")
    k = k-1
    print("")
        
k = 0
for i in range(row-1, 0, -1):
    for j in range (0, k+2):
        print (end = " ")
    for j in range (0, i):
        print(symb, end = "")
    k=k+1
    print("")
