n = 5
k = round(n/2)*2
for i in range(0,n):
    for j in range(0,k+1,2):
        print (end = '')
    for j in range(0,i+1):
        print("*",end = '')
    k=k-2
    print()
    
