months = [
    "Months",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if date[:2].isalpha() and ("/" in date or "," not in date):
             continue
        month, day, year = date.strip().replace(",", "").replace("/", " ").split()
        # print (month, day, year)
        if month.isalpha():
                month = months.index(month)
        if int(day)<=31 and int(month)<=12:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
        else:
            continue
    except ValueError:
        pass
