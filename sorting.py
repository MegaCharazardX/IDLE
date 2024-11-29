num = int(input("Enter the number of elements : "))
a = []
sorteda = []
for i in range (0,num):
    elem = input("Enter the element : ")
    a.append(elem)
print("The original list is : ",a)
while a :
    mini = a[0]
    for i in a :
        if i < mini :
            mini = i
    sorteda.append(mini)
    a.remove(mini)
print("The sorted list is : ",sorteda)
        
    
