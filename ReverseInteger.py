num = int(input("Enter Number : "))
a = ""
while True :
    if num%10 == 0:
        break
    r = int(num%10)
    a = a+str(r)
    num = (num-r)/10

number_dict = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine",
    10 : "Ten"

}

print(int(a))
for i in range(len(a)):
    print(number_dict[int(a[i])], end=" ")
print()