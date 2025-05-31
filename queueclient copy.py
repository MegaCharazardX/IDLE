import queue1
obj = queue1.queue()
print ("This is a program to operate with Queue.")
while True:
    userchoise = input("Enter your option [1-> enqueue, 2-> dequeue, 3-> fetch queue, 4-> clear queue, 5 -> exit] :")

    if userchoise == None or userchoise == "" or userchoise.isdigit == False :
        print("!!!-> Invalid input <- Enter valid input !!!")
        continue
    else :
        userchoise = int(userchoise)
        if userchoise == 1 :
            while True :
                no_of_elem =input("Enter the no. elements to append : ")
                if no_of_elem.isdigit() :
                    intno=int(no_of_elem)
                    for i in range (0,intno):
                        elem =input("Enter the element :")
                        obj.enqueue(elem)
                    break
                else:
                    print("Enter a valid input")
                    continue
                
        elif userchoise ==2 :
            while True :
                        
                elem_to_remove = input("Enter the number to remove :")
                if elem_to_remove == None or elem_to_remove=="" or elem_to_remove.isdigit==False :
                    print("!!!Invalid input. Please enter valid input!!!")
                    continue
                else :
                    retdequeue = obj.dequeue(elem_to_remove)
                    if retdequeue =='0':
                        print("Queue is empty.")
                    elif retdequeue == '1' :   
                        print("No elements found in the queue")
                    else :    
                        print(retdequeue)
                    break
        elif userchoise == 3:
            print(obj.fetchlist())

        elif userchoise == 4 :
            print(obj.clearqueue())
            
        else:
            continueorquit = input("!!!Are you sure you want to quit?!!! Enter '1' to continue the program, Enter '2' to quit. : ")
            if continueorquit == '1':
                continue
            else :
                print ("Thank you.")
                break       
