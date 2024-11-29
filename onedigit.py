print("This is a program to find the least of two one digit no.")
"""while True :
    no1 = int(input("Enter the first no. : "))
    no2 = int(input("Enter the second no. : "))
    if (no1 < 10) and (no2 < 10 ):
        if no1 > no2 :
            print ("The greatest number is : ",no1)
        else :
            print ("The greatest number is : ",no2)        
    else :
        print("Enter an one digit number !!!")
        continue
    deci = int(input("Do you want to try again ???(1 - try again ; 2 - quit ):"))
    if deci == 1 :
        continue
    else :
        print ("Thank you !!!")
        break
            
"""
while True :
    no1 = "789"#input("Enter the first no. : ")
    no2 = "321"#input("Enter the second no. : ")
    if no1.isdigit() and no2.isdigit() :
        #print ("hi")
        list1 = list(no1)
        list2 = list(no2)
        last1 = list1[-1]
        last2 = list2[-1]
        if last1 > last2 :
            print(last1)
        else:
            #sadfjkh
            pass
             
        print(list1,list2)
        print (last1,last2)
        break
    else  :
        print("Bye")
        continue











