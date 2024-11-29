#!/usr/bin/python3

import time
import sys
from time import sleep
from colorama import init, Fore

def trial():
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    str = "Current Time:" + time.asctime(t)
    return str

for i in range(1):
    #time.sleep(2.5)
    print(trial())


animation = "|/-\\"
start_time = time.time()
while True:
    for i in range(4):
        time.sleep(0.1)  # Feel free to experiment with the speed here
        sys.stdout.write("\rHari" + animation[i % len(animation)])
        sys.stdout.flush()
    if time.time() - start_time > 2:  # The animation will last for 10 seconds
        break
sys.stdout.write("\rDone!")

init()

def tprint(words):
    for char in words:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()

print(Fore.BLUE)
#tprint(Fore.RED = "This is just a color test.")
tprint("This is some example Text.")