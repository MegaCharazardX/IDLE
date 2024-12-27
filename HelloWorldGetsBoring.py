import time
import sys
import string

search = "Hello"
count = 0
OPsearch = ""

letters = string.printable
#print(letters)
while True :
    if OPsearch == search:
        break
    for current_Letter in search :
        to_break = False
        for letter in letters :
            time.sleep(0.02)
            sys.stdout.write(f"\r{OPsearch}" + letter)
            sys.stdout.flush()
            
            if  OPsearch == search or letter == current_Letter :
                OPsearch = OPsearch + letter
                count +=1
                to_break = True
                
            if to_break == True :
                break