# Emojize Problem


import emoji

def main():
    message = input("Input: ")
    output = emoji.emojize(message, language='alias')
    print("Output: ",output)

if __name__ == "__main__":
    main()
