

catalogue = (
    ("P101", 250, 40),
    ("P102", 99, 5),
    ("P103", -50, 20),
    ("P104", 1200, 8),
    ("P105", 75, -3),
)

total_value = 0
print("Invalid records:")
for pid, price, stock in catalogue:          # tuple unpacking
    if price <= 0 or stock < 0:
        print("  ", pid, "-> price:", price, "stock:", stock)

print("\nValid records and inventory value:")
for pid, price, stock in catalogue:
    if price > 0 and stock >= 0:
        value = price * stock
        total_value = total_value + value
        print("  ", pid, "| Value:", value)

print("\nTotal inventory value: Rs", total_value)

print("\nItems needing replenishment (stock < 10):")
for pid, price, stock in catalogue:
    if price > 0 and 0 <= stock < 10:
        print("  ", pid, "| Current stock:", stock)
