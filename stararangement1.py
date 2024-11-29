class Arange_stars:

    def aranging (self , symboltouse , nooflines ):
        patern = ""
        for i in range(int(nooflines)):
            patern +=symboltouse
            print(patern)
        
        




obj = Arange_stars()
strng = input ("Enter the symbol you want to print :")
while True:
    line = input ("Enter the no. of lines you want to print :")
    if line.isdigit () == True:
        obj.aranging(strng,line)
        break
    else :
        print("!!! Invalid input!!! Enter  a number")
