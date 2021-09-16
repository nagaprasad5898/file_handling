import os
file = open("cheat.txt", "a+")
file.write("hi frnds")
file.seek(0)
#os.lseek(file, 0, 0)
text = file.read()
print(text)