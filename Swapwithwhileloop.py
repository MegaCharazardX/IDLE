print("This is a program to swap numbers")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
continueorquit = 1
while continueorquit == 1 :
    input1=input("Enter the first number : ")
    input2=input("Enter the second number : ")
    if input1==input2 :
        print("Please enter different values")
        continue
    else :
        print("Before swaping first vaue is",input1,"and second vaue is",input2)
        temp=input2
        input2=input1
        input1=temp
        print("After swaping first vaue is",input1,"and second vaue is",input2)
#else :
    continueorquit=input("To continue enter 1 , to quit enter any other : ")
    continueoption = str.isnumeric(continueorquit)
    #print (continueoption)
    if str.isnumeric(continueorquit) and str.isnumeric(continueorquit) == 1 :
        continueorquit = 1
        continue
    else :
        break
print("Thank you")
