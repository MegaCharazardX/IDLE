print('This is the program to arange stars ')
typeofarrangement=int(input("Please enter the shape of the arrangement: "))

while typeofarrangement == 2:
    displaychar=input('Enter the Type of character to display : ')
    startcharcount=int(input('Enter the starting count : '))
    starcount=int(input('Enter the level of count : '))
    if startcharcount > starcount :
        print("Enter a value higher than the starting count the level")    
    
    for i in range(startcharcount,starcount+1):
        for j in range(0,i):
            if i >=3 :
                if j==0 or j == i :
                    print(displaychar,end=' ')
                else:
                    print("",end=' ')
            elif i == starcount:
                print(displaychar,end=' ')
                
            else :
                print(displaychar,end=' ')
    else :
        continueorquit=input("To continue enter 'C' , to quit enter any other ")
        
        if continueorquit=='C' :
            continue
        else:
            break
            print("Thank you")
        