class queue :
    
    def __init__(self):
        self.queue = []

        
    def fetchqueue (self):
        if len(self.queue)==0:
            return"No elements found."
        else:
            return self.queue
           
    def enqueue (self,element):
            self.queue.append(element)
            
            """if elem == i :
                print("!!!This element already exist!!!")
                continue
            else :
                print ("Hi")
                tmpqueue.append(elem)"""
            #return tmpqueue
    
    def dequeue(self,ele_to_remove):
        elementremoved = False

        for i in  self.queue :
            if elem_to_remove == i :
                elementremoved = True
                self.queue.remove(ele_to_remove)
        if (elementremoved):
            return "Element successfully removed."
        else :
            return "Element not found."
                
    def clearqueue (self):
        self.queue.clear()
        return "Queue is successfully cleared. "  
            


obj = queue()    
while True :
    userchoise =input("Choose your choise [1->enqueue 2->dequeue 3->display 4->clear 5->exit.] :")
    if userchoise == None or userchoise == "" or userchoise.isdigit ==False :
        print("Invalid input. Please enter valid input")
        continue
    else :
        userchoise = int(userchoise)
        if userchoise==1:
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
                    print("Invalid input. Please enter valid input")
                    continue
                else :
                    retdequeue = obj.dequeue(elem_to_remove)
                    print(retdequeue)
                    break
        
        elif userchoise == 3 :
            print(obj.fetchqueue())

        elif userchoise == 4 :
            print(obj.clearqueue())
            
        else:
            break

        
        

