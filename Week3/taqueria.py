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

def main():
    while True:
        try:
            item = input("Enter Item: ")
            result = menu_items[item]
            total = float(calculation(result))
            print (f"Total: {total}$")

        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a valid fraction.")
        except ValueError:
            print("Invalid input. Please enter the fraction in the format 'numerator/denominator'.")


def calculation(total, result):
    total += result
    return answer

answer = 0
main()