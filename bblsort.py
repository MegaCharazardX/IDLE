fst = []
#v1
n = int(input("Enter number of elements :"))
for i in range (0,n):
    ele = int (input ("Enter the element : "))
    fst. append (ele)
print("Original list :",fst)
l=len(fst)

#nextindex = currentindex+1
listsorted = False
while not(listsorted ) :
    currentindex = 0
    listsorted = True
    for j in range(0,l-1):
        if currentindex < (l-1 ):
            if fst[currentindex] > fst[currentindex+1]:
                listsorted = False
                #swaping
                temp = fst[currentindex+1]
                fst[currentindex+1] = fst[currentindex]
                fst[currentindex] = temp
                print(fst)
                currentindex = currentindex+1
    if not listsorted :
        continue
print("The sorted list is : ",fst)
   
