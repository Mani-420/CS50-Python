def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):    
    if 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha():
        for character in s:
            if character.isdigit():
                first = s.index(character)
                if s[first: ].isdigit() and int(character) != 0:
                    return True
                else:
                    return False
        return True


if __name__ == "__main__":
    main()