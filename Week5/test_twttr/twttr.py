def main():
    cool_string = input("Enter a string: ")
    answer = shorten(cool_string)
    print (answer)


def shorten(word):
    ans_string = ""
    for character in word:
        if (character not in ["A", "a", "E", "e", "I", "i", "O", "o", "u", "U"]):
            ans_string += character
    return ans_string


if __name__ == "__main__":
    main()