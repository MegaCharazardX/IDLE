while True :
    class ListDemo :
        
        

        def CreateList(self , _list_items):
            self.listItem = _list_items
            print('List created ...')
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-        
        def ReadList (self,_should_sort = False):
            tmplistitem = self.listItem
            if (_should_sort) :
                tmplistitem = sorted(tmplistitem)            
            return tmplistitem
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
        def GetListSize(self,_item_to_count = None ):        
            if _item_to_count == None :
                tmplistitem = self.listItem
            else :
                tmplistitem = _item_to_count     
            return len(tmplistitem)
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
        def InsertList(self, _where_to_insert,_item_to_be_inserted, _should_insert = False):
            tmplistitem = self.listItem
            if (_should_insert) :
                list.insert(tmplistitem, _where_to_insert, _item_to_be_inserted )          
            return tmplistitem
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
        def AppendList(self,_item_to_be_appended, _should_append = False):
            tmplistitem = self.listItem
            if (_should_append) :
                list.append(tmplistitem, _item_to_be_appended )          
            return tmplistitem
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- 
        def Slicelist(self,_lower_index,_higher_index,_should_slice =  False ):
            tmplistitem = self.listItem
            if (_should_slice):
                list[_lower_index:_higher_index] 
            return tmplistitem    
                
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
           
    obj = ListDemo ()

    obj.CreateList(list(input ('Please enter the elements of the list : ')))

    print('Before sort')
    retlistitem = obj.ReadList()
    print('List before sorting : ',end  = '')
    print(retlistitem)

    print('After sort')
    retsortedlist = obj.ReadList(True)
    print('List after sorting : ',end  = '')
    print(retsortedlist)

    #Showing size after sorting
    retlistsize = obj.GetListSize(retlistitem)
    print('Showing size after sorting : ',retlistsize,'.')


    print('After inserting')
    retinsertedlist = obj.InsertList(int(input('Please enter the position to insert : ')),str(input('Please enter the number to insert : ')),True)
    print('List after inserting : ',end  = '')
    print(retinsertedlist)

    #Showing size after inserting
    retinsertedlistsize = obj.GetListSize(retlistitem)
    print('Showing size after inserting',retinsertedlistsize)

    print('Appending value(s) into the list , 4')
    retappendedlist = obj.AppendList(input("Please enter the element(s) for ammending"),True)
    print('List after appending : ',end  = '')
    print(retappendedlist)

    #Showing size after appending and inserting
    retappendedlistsize = obj.GetListSize(retlistitem)
    print("Showing size after appending and inserting : ",end = '')
    print(retappendedlistsize)

    #Silicing the list
    print('Slicing the list ')
    retslicedlist = obj.Slicelist(int(input("Please enter the lowest position : ")),int(input("Please enter the highest position : ")),True)
    print("Showing the elements after slicing : ",end = '')
    print(retslicedlist)

    continueorquit=int(input("To continue enter 1 , to quit enter any other : "))
    if continueorquit == 1 :
        continue
    else :
        break
        print("Thank you")
    
