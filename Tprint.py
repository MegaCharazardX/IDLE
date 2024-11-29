import sys
from time import sleep


def tprint(word, interval = 0.015):
    for char in word:
        sleep(interval)
    #     print(char, end = "")
    # print("\n")
        sys.stdout.write(char)
        sys.stdout.flush()
        
        
# tprint("Hello. This Hari Dhejus V.S. of grade 12.")

# pre = "Mrs"
# gender = "boy"
# if gender == "boy":
#     pre = "Mr"
    
# print(pre)