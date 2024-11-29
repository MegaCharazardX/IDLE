from Tprint import tprint

def _odd(x):
     if (2*x + 1) < n :
    #     pass
    # else:
        return 2*x + 1

def _even(x):
    if (2*x) < n :
    #     pass
    # else:
        return 2*x

odd_list, even_list = [], []

tprint(f"Enter the upperbound : ")
n = int(input())

for i in range(n):
    if _odd(i) != None :
        if _odd(i) !=n :
            odd_list.append(_odd(i))
    if _even(i) != None :
        if _even(i) !=n :
            even_list.append(_even(i))
    
tprint(f"The odd number(s) upto {n} are {odd_list}\n")
tprint(f"The even number(s) upto {n} are {even_list}")