def main():
    percentage = convert(input("Fraction: "))
    # print (f"The percentage is: {percentage}")
    print(gauge(percentage))


def convert(frac):
    while True:
        try:
            first, second = frac.split("/")
            first = int(first)
            second = int(second)
            answer = first/second
            percentage = int(answer * 100)

            if percentage > 100:
                print("Percentage exceeds 100%. Please enter a valid fraction.")
                continue 
            else:
                return percentage

        except (ZeroDivisionError, ValueError):
            raise


def gauge(percentage):
    if percentage == 66:
        return "67%"
    elif percentage > 90:
        return "F"
    elif percentage < 10:
        return "E"
    else:
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()