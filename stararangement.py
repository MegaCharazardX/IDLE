print('This is the program to arange stars ')
print("====================================")
print('Triangle = 1/Prramid = 2')
typeofarrangement=int(input("Please enter the shape of the arrangement: "))
while typeofarrangement == 1:
    #rowno = int(input("Enter the row count : "))
    #colno = int(input("Enter the column count : "))
    displaychar=input('Enter the Type of character to display : ')
    startcharcount=int(input('Enter the starting count : '))
    starcount=int(input('Enter the level of count : '))
    if startcharcount > starcount :
        print("Enter a value higher than the starting count the level")    
    #starcount=int(input('Enter the level count : '))
    for i in range(startcharcount,starcount+1):
        #print(i*displaychar)
        #print('\n')
        for j in range(0,i):
            print(displaychar,end=' ')
        print('\n')
    else :
        continueorquit=input("To continue enter 'C' , to quit enter any other ")
        
        if continueorquit=='C' :
            continue
        else:
            break
            print("Thank you")
        
#elif typeofarrangement == 2 :
    



        
