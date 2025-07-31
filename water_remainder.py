import pyttsx3
import time
import os
engine = pyttsx3.init()
def speak_remainder():
    engine.say("Drink Water")
    engine.runAndWait()

while True:
    time.sleep(10800)
    command = "osascript -e \'say \"Hey Harry drink water\"\'; osascript -e \'display alert \"Hey Harry, Drink water\"\'"
    os.system(command)
    speak_remainder()

