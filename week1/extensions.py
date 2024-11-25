def main():
    file = input("Enter your File name: ").lower().strip()
    answer = check(file)
    print (answer)
    

def check(file):
    if file.endswith(".gif"):
        return "image/gif"
    
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        return "image/jpeg"
    
    elif file.endswith(".png"):
        return "image/png"
    
    elif file.endswith(".pdf"):
        return "application/pdf"
    
    elif file.endswith(".text") or file.endswith(".txt"):
        return "text/plain"
    
    elif file.endswith(".zip"):
        return "application/zip"
    
    else:
        return "application/octet-stream"


if __name__ == "__main__":
    main()
