# Grocery List Problem


grocery_list = {}

i = 0                       # Only if you want to check the working of program
while i < 5:                # Only if you want to check the working of program
    try:
        item = input("Enter Items: ").upper()
        i += 1              # Only if you want to check the working of program

        if item in grocery_list:
            grocery_list[item] += 1
            
        else:
            grocery_list[item] = 1

    except KeyError:
        pass

    except EOFError:
        print("\n")
        break
    
for item in sorted(grocery_list.keys()):
    print(f"{grocery_list[item]} {item}")
