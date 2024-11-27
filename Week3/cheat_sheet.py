# -----------------------------------------------------------------------

# try:
#     x = int(input("Enter a number: "))

# except ValueError:
#     print("X is not an integer.")

# else:
#     print(f"x is {x}")

# -----------------------------------------------------------------------

# while True:
#     try:
#         x = int(input("Enter X: "))

#     except ValueError:
#         print("X is not an integer.")

#     else:
#         break

# print(f"x is {x}")

# -----------------------------------------------------------------------

# while True:
#     try:
#         x = int(input("Enter X: "))
#         break

#     except ValueError:
#         pass

# print(f"x is {x}")

# -----------------------------------------------------------------------

# def main():
#     x = get_int()
#     print (f"X is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("Enter X: "))

#         except ValueError:
#             pass

# main()

# -----------------------------------------------------------------------

def main():
    x = get_int("Enter X: ")
    print (f"X is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass

main()