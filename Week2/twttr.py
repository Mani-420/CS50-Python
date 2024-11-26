def main():
    cool_string = input("Enter a string: ")
    ans_string = ""
    answer = convert(cool_string, ans_string)
    print (answer)

def convert(cool_string, ans_string):
    
    for character in cool_string:
        if (character not in ["A", "a", "E", "e", "I", "i", "O", "o", "u", "U"]):
            ans_string += character

        else:
            continue

    return ans_string

main()