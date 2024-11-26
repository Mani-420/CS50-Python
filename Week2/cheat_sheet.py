# code = {
#     "aaiz": 96,
#     "azib": 56,
#     "Mani": 25,
#     "Abdullah": 10,
#     "hamza": 992,
# }

# def main():
#     for name in code.keys():
#         print(f"{name} secret code is {code[name]}.")

# main()


def main():
    amount_due = 50
    print (f"Amount Due: {amount_due}")
    convert(amount_due)

def convert(amount_due):

    while amount_due > 0:

        insert_amount = int(input("Insert Coin: "))
        print (f"Amount Due: {amount_due}")

        if amount_due < insert_amount:
            change = insert_amount - amount_due
            print (f"Amount Due: {amount_due}")
            print (f"Change Owed: {change}")

        if insert_amount == 25 or insert_amount == 10 or insert_amount == 5:
            amount_due -= insert_amount

            if amount_due < 0:
                amount_due = 0
                break

            print (f"Amount Due: {amount_due}")

        else:
            continue

main()
