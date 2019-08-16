change = round(float(input("Change: ")) * 100)
if change <= 0:
    change = round(float(input("Change: ")) * 100)
print(change)
coins = 0
quarter = 0
dime = 0
nickel = 0
penny = 0

while change > 0:
    while change >= 25:
        change -= 25
        quarter += 1
    while change >= 10:
        change -= 10
        dime += 1
    while change >= 5:
        change -= 5
        nickel += 1
    while change >= 1:
        change -= 1
        penny += 1

coins = quarter + dime + nickel + penny
print("You get %i coins: %i quarter(s), %i dime(s), %i nickel(s) and %i pennie(s)."%(coins,quarter, dime, nickel, penny))
