print("This is a program to find if a number is prime or not.")
class  PrimeNumber :
    def finding_prime(self,number):
        number = int(number)
        if number == 1 or number == 2 or number == 3  :
            prime = 'This is prime'
            return prime
        for i in range(2,number-1):    
            if number%i == 0 :
                notprime = 'This number is not  prime.',[int(number/i),i],'are the first pair of factors.'
                return notprime
        for i in range(2,number-1):    
            if number%i !=0:
                prime = 'This is prime'
                return prime
        
obj = PrimeNumber()
while True :
    number = input("Enter the number to check if it is prime :")
    if number == None or number.isdigit()==False:
        print('Invalid Input')
    else :
        retval = obj.finding_prime(number)
        print(retval)
        desision = input("Do you want to go again ? Enter '1' to go again/ and any other  to exit :")
        if desision=='1':
            print("Here we go...")
            continue
        else:
            print("Thank you")
            break
                
            
