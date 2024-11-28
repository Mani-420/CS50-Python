import random

def game(level):
    guess = random.randint(1, level)
    while True:
        try:
            answer = int(input("Guess: "))
            if answer < guess:
                print("Too small!")
            elif answer > guess:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:  # Ensuring the level is positive
                game(level)
                break  # Exits the loop after the game finishes
            else:
                print("Level must be a positive integer.")
        except ValueError:
            pass

if __name__ == "__main__":
    main()
