n = int(input("Enter number : "))
isEven = True
for i in range(2, n):
    if isEven == True:
        isEven=False
    else:
        isEven = True
    
if isEven==True:
    print("Even")
else:
    print("Odd")