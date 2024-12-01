import tabulate
import sys
import csv


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    file_name = sys.argv[1]
    if file_name.endswith(".csv"):
        try:
            with open(file_name, "r") as file:
                reader = csv.DictReader(file)
                print (tabulate.tabulate(reader, headers = "keys", tablefmt = "grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("File does not exist")
