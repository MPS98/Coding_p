change = round(float(input("Change: ")) * 100)
if change <= 0:
    change = round(float(input("Change: ")) * 100)
# print(change)
coin_dict = {
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }

coin_list = list(coin_dict.values())
# print(coin_list)
coin_count = 0

for i in range(0,4):
    print(coin_list[i])

if change == 0:
    print(coin_count)
else:
    while change >= coin_list[i]:
        print(coin_list[i])
        change -= coin_list[i]
        coin_count += 1
    i += 1
