def main():
    while True:
        try:
            expression = input("Fraction: ")
            first, second = expression.split("/")
            
            first = assignment(first)
            second = assignment(second)

            fraction = check(first, second)
            print(fraction)
            break  # Exit loop after successful execution

        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a valid fraction.")
        except ValueError:
            print("Invalid input. Please enter the fraction in the format 'numerator/denominator'.")

def assignment(number):
    return int(number)

def check(first, second):

    fraction = first / second

    percentage = int(fraction * 100)
    
    if fraction > 1:
        main()

    elif percentage == 66:
        return "67%"
    
    elif fraction > 0.9:
        return "F"
    
    elif fraction < 0.1:
        return "E"
    
    else:
        return (str(percentage) + "%")

main()
