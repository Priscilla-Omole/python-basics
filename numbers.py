# Handle proper error with the appropriate messages
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
        while True:
            try:
                return int(input("What is x? "))
            except ValueError:
                pass #Still catch the error but not do anything about it.
        
main()
