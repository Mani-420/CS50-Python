# -----------------------------------------------------------------------------
# How to write in a file:--------------------------------


# name = input("What' your name: ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# ---------------------------------------------------------------------------
# How to read from a existing file:--------------------------------


# with open ("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     # print("Hello,", line, end="")
#     print("Hello,", line.rstrip())


# ---------------------------------------------------------------------------
# How to read from a existing file:--------------------------------


with open ("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
