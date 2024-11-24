# Tip Calculator


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # print(dollars)
    # print(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    sign = d.replace("$", "")
    money = float(sign)
    return money

def percent_to_float(p):
    sign = p.replace("%", "")
    tip = float(sign)
    cash = tip/100
    return cash

main()