#open and print content in file
name= input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())

#read and sort.
names= []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse= True):
    print(f"hello, {name}")