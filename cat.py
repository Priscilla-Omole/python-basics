def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n= int(input("What's n? "))
        if n > 0:
            break
    return n  

    for i in range(n):
        print("meow")


main()



# while True:
#     n = int(input("What is n? "))
#     if n > 0:
#         break

# for i in range(n):
#     print("meow")




# for i in range(3):
#     print("meow")

# #You can easily replace a variable thatis not really in use, like i, in this case. 
# #It is just present for the for loop.

# for _ in range(3):
#     print("meow")

# print("meow \n" * 3, end="")