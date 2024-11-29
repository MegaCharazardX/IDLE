
#numberofelem = int(input("Enter the maximum number of fibonacci series: "))
class fibo :
    def __init__(self):
        self.nxtnumberlist = [0,1]
        
    def findfibo(self,numberofelem):
        num1 = 0
        num2 = 1
        nxtnum = num2
        for i in range (2,numberofelem):
            nxtnum = num1 +num2
            num1 = num2
            num2 = nxtnum
            self.nxtnumberlist.append(nxtnum)
        return self.nxtnumberlist

    def findelem(self,numbertofind):
        if (numbertofind in self.nxtnumberlist):
            return "This element is fibonaci"
            
        else :
            return "This element is not fibonaci"

    def findsection (self,lowerbound,upperbound):
        retlist1 = obj.findfibo(upperbound)
        lis = retlist1[lowerbound:upperbound]
        return lis
        


obj = fibo()
retlist = obj.findfibo(int(input("Enter the maximum number of fibonacci series: ")))
print(retlist)

retstr = obj.findelem( int(input("Enter the number to find : ")))
print(retstr)


retsection = obj.findsection(int(input("lowerer bound:")),int(input("upperbound :")))
print("There are ",len(retsection),"between the interval you entered.")
print(retsection)











"""nextnumber = num2
nextnumberlist = [0,1,num2]
count = 1
#=-=-=-=-=-=-=-=-
while count < numberofelem -2 :
    count+=1
    num1,num2 = num2,nextnumber
    nextnumber = num1 + num2
    nextnumberlist.append(nextnumber)
print(nextnumberlist)
#=-=-=-=-=-=-=-=-=-
numbertofind = int(input("Enter the number to find : "))
if (numbertofind in nextnumberlist):
    print("This element is fibonaci")
    
else :
    print("This element is not fibonaci")



while True :
    maxrange =input("Enter the maximum range :")
    if maxrange == None or maxrange == "" or maxrange.isdigit ==False :
        print("Invalid input. Please enter valid input")
        continue
    else :
        maxrange = int(maxrange)
        for i in range(0,maxrange):
            initial = initial + i
            print(initial)
        break
"""
