

tax_rates = {"Grocery": 5, "Clothing": 12, "Electronics": 18}


items = [
    ("Rice", "Grocery", 60, 10),
    ("T-Shirt", "Clothing", 500, 3),
    ("Headphones", "Electronics", 1500, 2),
]

subtotal = 0
total_tax = 0

print("Item         Qty   Price    Tax     Total")
print("-" * 45)
for name, category, price, qty in items:      # tuple unpacking
    amount = price * qty
    tax = amount * tax_rates[category] / 100
    subtotal = subtotal + amount
    total_tax = total_tax + tax
    print(name.ljust(12), str(qty).ljust(5), str(amount).ljust(8),
          str(round(tax, 2)).ljust(7), round(amount + tax, 2))

discount = 0
if subtotal > 5000:
    discount = subtotal * 0.10
    if discount > 500:
        discount = 500

final = subtotal + total_tax - discount
print("-" * 45)
print("Subtotal :", subtotal)
print("Tax      :", round(total_tax, 2))
print("Discount :", discount)
print("Final Bill:", round(final, 2))
