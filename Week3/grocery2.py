items = []
i = 1

while i<5:
    try:
        item = input("Enter Item: ").upper()
        i += 1

    except EOFError:
        print("\n")
        break

    if item in items:
        continue
    else:
        items.append(item)

    
for i in items:
    print(f"{i}")