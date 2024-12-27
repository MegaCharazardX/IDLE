num = int(input("Enter the number to check if fibonaaci : "))
F = []
n = num //2+3
for i in range (n):
    if i == 0 :
        F.extend([0,1])
    else:   
        F.append(F[-1]+F[-2])
print(F)
if num in F:
    print(f"{num} is the {F.index(num) +1}(th) element in the fibonaaci series.")
else:
    print(f"The number {num} is not a fibonaaci number")
