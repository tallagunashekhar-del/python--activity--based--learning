

n = int(input("Enter size of diamond (3 to 15): "))

if n < 3 or n > 15:
    print("Invalid size! Enter a number between 3 and 15.")
else:
    # upper half
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        if i == 1:
            print("*")
        else:
            print("*" + " " * (2 * i - 3) + "*")

    # lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        if i == 1:
            print("*")
        else:
            print("*" + " " * (2 * i - 3) + "*")
