import sys
import csv


def main():
    check_command_line()
    result = []
    try:
        file1_name = sys.argv[1]
        file2_name = sys.argv[2]

        with open (file1_name, "r") as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                last_name, first_name = row["name"].split(",")
                full_name =  first_name + " " + last_name
                # print(full_name)
                result.append({"first": first_name.lstrip(), "last": last_name, "house": row["house"]})

        with open (file2_name, "w") as file2:
            writer = csv.DictWriter(file2, fieldnames=["first","last","house"])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            for row in result:
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

    except FileNotFoundError:
        sys.exit("File not found")


def check_command_line():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("CSV file not found")


if __name__ == "__main__":
    main()
