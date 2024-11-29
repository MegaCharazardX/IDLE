from prettytable import PrettyTable
x = int(input("Enter A Number : "))
num_of_elem = x**2

elem_list = []
elem_list = elem_list[::-1]
for i in range(num_of_elem):
    elem_list.append(i+1)

seperatedList = []
count = 0
for i in range(x):
    elem = elem_list[count:x+count]
    count +=x
    seperatedList.append(elem)

for i in seperatedList[::-1]:
    for j in i :
        if j < 10:  
            print(f"{j} ", end=" ")
        elif j < 100:
            print(f"{j}", end= " ")
    print()

print(f"{"-"*10} Thank You {"-"*10}")