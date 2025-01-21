num = int(input("Enter Number : "))
rem = 0
rev = 0
while num!=0:
    rem = int(num%10)
    rev = int(rev*10 + rem)
    num = int(num/10)

print(rev)