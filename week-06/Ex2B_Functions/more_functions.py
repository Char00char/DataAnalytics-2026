def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f"{city}, {state} {zip_code}")

display_mailing_label("Charles Palacios", "123 Main St", "Sterling", "VA", "20166" )
print()
display_mailing_label("Jane Doe", "456 Elm St", "Springfield", "IL", "62704")    

def add_numbers(*args):
    total = sum(args)
    expression = " + ".join(str(num) for num in args)
    print(f"{expression} = {total}")

add_numbers(1, 2, 3)
add_numbers(4, 5, 6, 7)
add_numbers(8)

def display_receipt(total_due, amount_paid):
    change = amount_paid - total_due

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if amount_paid < total_due:
        print(f"Remaining Balance: ${abs(change):.2f}")
    else:
        print(f"Change Due: ${change:.2f}")

display_receipt(20, 30)
print()

display_receipt(15, 15)
print()

display_receipt(50, 20)
print()

