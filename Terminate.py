import os
import string
import sys
import time
from random import Random
import random

letters = string.printable    
prepNote= "Preparing to remove System32..."

def tprint(word, interval = 0.015):
    for char in word:
        time.sleep(interval)
        #print(char, end = "")
    # print("\n")
        sys.stdout.write(char)
        sys.stdout.flush()
        
def prep_(search):
    count = 0
    OPsearch = ""
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

isAutherized = False
f = open("SYS32INFO.txt", "r")
try : 
    def t():
        global Info
        Info = f.read()

        tprint("Enter password : ")
        pwd = input()

        if pwd != "Charazard101" :
            tprint("Not Autherised"+ "\n")
            tprint(prepNote+ "\n")
            time.sleep(0.5)
            tprint("Removing... ")
            tprint(f"                   {Info}", interval = 0.0000002)
        else:
            global isAutherized
            isAutherized = True
            tprint("Hello Hari ... Seems like its bit of a hurry ...! Removing all files\n")
            time.sleep(0.5)
            tprint(prepNote+ "\n")
            #prep_("Deleting System 32..." + "\n")
            tprint("Removing... ")
            tprint(f"                   {Info}", interval = 0.0000002)
    t()
        
except KeyboardInterrupt :
    if isAutherized == True :
        tprint(f"\nClose call Hari {random.randint(50, 99)}% removed..")
        tprint("\nCanceling Deletion...")
        tprint("\nRollbacking...")
        time.sleep(2)
        tprint("\nRollbacked")
        tprint("\nDeletion Canceled ...")
        
    else:
        tprint("\nUnAuthourized User...")
        tprint("\nThis is ther last chance, if You don't what you're doing ask Hari :")
        tprint("\nThis is ther last chance Enter password :")
        pwd2 = input()
        
        if pwd2 == "Charazard101":
            tprint(f"\nClose call Hari {random.randint(50, 99)}% removed..")
            tprint("\nCanceling Deletion...")
            tprint("\nRollbacking...")
            time.sleep(2)
            tprint("\nRollbacked")
            tprint("\nDeletion Canceled ...\nGood Day To you sir")
            time.sleep(2)
        else:
            tprint("Wrong password...")
            tprint("Continuing to delete...")
            tprint("Removing... ")
            tprint(f"                   {Info}", interval = 0.0000002)
            
        
f.close()
#os.remove