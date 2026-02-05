# def main():
#     print_column(3)
    

# def print_column(height):
#     for _ in range(height):
#         print("#")
# main()


# def main():
#     print_row(3)
    

# def print_row(width):
#     print("?" * 3)
# main()


def main():
    print_square(3)

def print_square(size):
    #For each row in square
    for i in range(size):
        print("#" * size)

main()