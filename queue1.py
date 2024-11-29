class queue :
    def __init__(self):
        self.queue = []


    def fetchlist(self)    :
        if len(self.queue) == 0:
            return "0"
        else :
            return self.queue


    def enqueue(self,element):
        self.queue.append(element)
        

    def dequeue(self,ele_to_remove):
        elementremoved = False
        if len(self.queue) == 0:
            return "0"
        else :
            for i in  self.queue :
                if ele_to_remove == i :
                    elementremoved = True
                    self.queue.remove(ele_to_remove)
            if (elementremoved):
                return "Element successfully removed."
            else:
                return "1"
            

    def clearqueue(self) :
        self.queue.clear()
        return "Queue successfully cleared."

