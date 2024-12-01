# --------------------------------------------------------------------------------------
# Method # 1: -------------------------------------------------------
# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
    
# for name in sorted(names):
#     print(f"Hello, {name}")



# --------------------------------------------------------------------------------------
# Method # 2: -------------------------------------------------------
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("Hello,", line.strip())



# --------------------------------------------------------------------------------------
# Changes to Data: -------------------------------------------------------

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names, reverse=True):
    print(f"Hello, {name}")