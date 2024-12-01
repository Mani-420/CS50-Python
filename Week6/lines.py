import sys
counter = 0


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    # counter = 1
    file_name = sys.argv[1]
    if file_name.endswith(".py"):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    if not line.lstrip().startswith("#") or line.strip().startswith(" "):
                        counter += 1
                print(counter)

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("File does not exist")
