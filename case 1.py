

def calculate_bill(units):
    if units <= 100:
        energy = units * 3
    elif units <= 200:
        energy = 100 * 3 + (units - 100) * 5
    else:
        energy = 100 * 3 + 100 * 5 + (units - 200) * 8

    bill = energy + 50              # add fixed charge

    if units > 300:
        bill = bill + bill * 0.10   # surcharge
    if units <= 100:
        bill = bill - bill * 0.05   # rebate
    return bill


months = ["Jan", "Feb", "Mar", "Apr", "May"]
units_used = [90, 150, 320, 210, 400]

previous_bill = 0
for i in range(len(months)):
    bill = calculate_bill(units_used[i])
    print(months[i], "| Units:", units_used[i], "| Bill: Rs", round(bill, 2), end="")
    # unusual increase = more than 30% jump from last month
    if previous_bill > 0 and bill > previous_bill * 1.30:
        print("  <-- Unusual increase!", end="")
    print()
    previous_bill = bill
