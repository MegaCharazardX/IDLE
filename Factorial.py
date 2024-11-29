fac_temp = 1
def Calculate_factorial(a):
    #fac = 1
    if a > 0 :
        #global fac_temp
        fac_temp = fac_temp * Calculate_factorial(a-1)
        fac = fac_temp
    print (fac)
    # f = 1
    # for i in range(1, a+1):
    #     f *= i
    # return f
    
num = int(input("Enter the number to find the factorial : "))
print(f"{num}! = {Calculate_factorial(num)}")