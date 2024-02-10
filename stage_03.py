with open("artifacts01.txt", "r") as f:
    text = f.read()

print(text)

with open("artifacts02.txt", "w") as f:
    f.write(text + " added few more lines.")

print("end of stage 3")
          