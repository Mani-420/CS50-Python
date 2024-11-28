# Little Professor Game


import random

def main():
    level = get_level()

    count = 1
    tries = 1
    score = 1

    while count <= 10:
        try:
            x, y = generate_integer(level)
            running = True
            while running:
                answer = int(input(f"{x} + {y} = "))
                if tries == 3:
                    print(f"{x} + {y} = {x+y}")
                    score -= 1
                    count += 1
                    running = False
                if answer == x + y:
                    count += 1
                    score += 1
                    running = False
                else:
                    tries += 1
                    print("EEE")
                    continue
        except ValueError:
            pass
    
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            total_levels = [1, 2, 3]
            level = int(input("Level: "))
            if level in total_levels:
                return level
                break
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y


if __name__ == "__main__":
    main()
