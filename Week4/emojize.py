import emoji

def main():
    message = input("Input: ")
    output = emoji.emojize(message, language='alias')
    print("Output: ",output)

main()
