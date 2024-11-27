# Taqueria Problem 


menu_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

answer = 0

while True:
    try:
        item = input("Enter Item: ").title()
        result = menu_items[item]
        total = float(result)
        answer += total
        print (f"Total: ${answer:.2f}")

    except KeyError:
        pass
    except ValueError:
        pass
    except EOFError:
        print("\n")
        break
