#Write & Append

# Libraty Delete        import os

f = open("contoh.txt", "a")
f.write("Added text")
f.close()

f = open("contoh.txt", "w")
f.write("Hello World")
f.close()

f = open("contoh.txt", "r")
print(f.read())

f = open("contoh.txt", "r")
print(f.read(5))

f = open("contoh.txt", "r")
print(f.readline())


# os.remove("contoh.txt")
