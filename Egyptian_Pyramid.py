lines = int(input("Enter the number of lines : "))
space = lines*2 
for i in range(1, lines+1):
    for j in range (0,space):
        print(end = " ")
    for j in range(i,0,-1):
        print(j, end = " ")
    for j in range (2,i+1):
        print(j, end = " ")
    space = space - 2
    print()

input()
