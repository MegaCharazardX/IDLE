num = int(input("Enter the number :"))
if num == 1 or num == 2 or num == 3:
    print("The number is prime")
else :
    shouldproceed = True
    for i in range(2,round(num/2)):
        if num % i == 0:
            print("This number is not prime")
            shouldproceed = False
            break
                
