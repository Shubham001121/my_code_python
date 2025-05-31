import os
i = 1
files = os.listdir("clutter1")
for file in files:
   if file.endswith(".png"):
     print(file)
     os.rename(f"clutter1/{file}",f"clutter1/{i}.png")
     i += 1

# os.remove("clutter1/1.png")