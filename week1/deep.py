def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    answer = check(question)
    print (answer)


def check(question):
    if question == "42" or question == "forty two" or question == "forty-two":
        return "Yes"
    else:
        return "No"
    
main()