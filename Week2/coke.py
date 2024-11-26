def main():
    amount_due = 50
    print (f"Amount Due: {amount_due}")
    inserted_coins= 0
    convert(amount_due, inserted_coins)

def convert(amount_due, inserted_coins):

    while amount_due > 0:
        
        insert_amount = int(input("Insert Coin: "))
        if insert_amount == 25 or insert_amount == 10 or insert_amount == 5:
            amount_due -= insert_amount
            inserted_coins += insert_amount

            if inserted_coins >= 50:
                print (f"Change Owed: {inserted_coins - 50}")
            
            else:
                print (f"Amount Due: {amount_due}")

        else:
            print (f"Amount Due: {amount_due}")
            insert_amount = int(input("Insert Coin: "))
    
main()