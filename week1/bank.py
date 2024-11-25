# Bank Problem 


def main():
    greeting = input("Enter your greetings: ").lower().strip()
    answer = check(greeting)
    print (answer)

def check(greeting):
    if greeting[0:5] == "hello":
        return "0$"
    
    elif greeting[0] == "h":
        return "20$"
    else:
        return "100$"

main()