import pyttsx3
engine = pyttsx3.init()
l = ["shubham","rahul","shivam","shivangi"]
for i in l:
  phrase = f"Shoutout to {i}"
  print(phrase)
  engine.say(phrase)
engine.runAndWait()
