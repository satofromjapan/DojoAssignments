def change(cents):
    coins = {}
    while cents > 0:
        if cents >= 100:
            coins["dollar"] = int(cents / 100)
            cents = cents % 100
        elif cents >= 25:
            coins["quarters"] = int(cents/25)
            cents = cents % 25
        elif cents >= 10:
            coins["dimes"] = int(cents/10)
            cents = cents % 10
        elif cents >= 5:
            coins["nickels"] = int(cents/5)
            cents = cents % 5
        else:
            coins["pennies"] = cents
            cents = cents % 1
    return coins



print change(387)
