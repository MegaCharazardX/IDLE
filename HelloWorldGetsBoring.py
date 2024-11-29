import time
import sys
import string

# start_time = time.time()

# def loading(animation = "|/-\\", startTime = 5, text = "Hi. On behalf of Loading Community ! ", speed = 0.2):
#         while True:
#             for i in range(10):
#                 time.sleep(speed)  # Feel free to experiment with the speed here
#                 sys.stdout.write(f"\r{text}" + animation[i % len(animation)])
#                 sys.stdout.flush()
#             sys.stdout.flush()
#             sys.stdout.write(f"\r{text}" + " ")
#             sys.stdout.flush()
#             if time.time() - start_time > startTime:  # The animation will last for 10 seconds
#                 sys.stdout.flush()
#                 break
            
# loading(text= " Hello World")

Text = "Hello" # Input
count = 0
OPText = ""
letters = string.ascii_letters + " "
while True :
    if OPText == Text:
        break
    for letter in letters :
        time.sleep(0.02)
        sys.stdout.write(f"\r{OPText}" + letter)
        sys.stdout.flush()
        if OPText == Text:
            break
        if  letter == Text[count] :
            OPText = OPText + letter
            count +=1
    break