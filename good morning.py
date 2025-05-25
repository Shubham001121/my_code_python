#GOOD MORNING
import time  
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp = int(time.strftime("%H"))

if (5 <= timestamp < 12):
    print("good morning")
elif(12 <= timestamp <17):
    print("good afternoon")
elif(17 <= timestamp <20):
    print("good evening")
else:
    print("good night")