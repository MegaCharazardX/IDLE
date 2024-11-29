print('Program to find the power for given base and exponential')
print('========================================================')
baseno=int(input("Enter the base : "))
exponent=int(input("Enter the exponent : "))
ans=1
if exponent<0:
    print("Please enter exponent greater than 0")
elif exponent==0:
    print("The answer is 1.")
elif exponent==1:
    print("The answer is ",baseno,'.')
else:
    for currentpower in range(0,exponent):
        ans=ans*baseno

    print('The answer is ',ans,'.')
        

  
