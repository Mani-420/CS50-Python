# Camel case to snake case 


def main():
    camelCase = input("Enter in camel case: ")
    snake_case = ""
    answer = convert(camelCase, snake_case)
    print (answer)

def convert(camelCase, snake_case):
    
    for character in camelCase:
        if character.isupper():
            snake_case = snake_case + "_" + character.lower()
        else:
            snake_case += character

    return snake_case

if __name__ == "__main__":
    main()
