def main():
    expression = input("Enter your expression: ")
    x,y,z = expression.split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        print(x+z)
    
    elif y == "-":
        print(x-z)
    
    elif y == "*":
        print(x*z)
    
    elif y == "/" and z != 0:
        print(x/z)

    else:
        return "Invalid Input."

main()