print("Welcome to CATUC POS")
num_items = int(input("Please enter the number of items: "))

# Each item is stored as a dictionary
items = []
for i in range(1, num_items + 1):
    print(f"\n--- Item {i} ---")
    name = input("Description (item name): ")
    quantity = int(input("Quantity: "))
    unit_price = float(input("Unit price: "))
    items.append({
        "name": name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total": quantity * unit_price,
    })

# Sub-total before discount
items_cost_total = sum(item["total"] for item in items)

# Discount rules (same as in class)
if items_cost_total > 10000:
    discount_rate = 0.30
elif len(items) > 5 and items_cost_total > 4000:
    discount_rate = 0.15
elif items_cost_total > 5000:
    discount_rate = 0.10
else:
    discount_rate = 0

discount = discount_rate * items_cost_total
total_cost = items_cost_total - discount

# ---------- Receipt ----------
line = "=" * 62
print("\n" + line)
print("CATUC POS - SAMPLE RECEIPT".center(62))
print(line)
print(f"{'S/N':<5}{'Description':<22}{'Qty':>5}{'Unit Price':>14}{'Total Price':>16}")
print("-" * 62)

for sn, item in enumerate(items, start=1):
    print(f"{sn:<5}{item['name'][:20]:<22}{item['quantity']:>5}"
          f"{item['unit_price']:>14,.2f}{item['total']:>16,.2f}")

print("-" * 62)
print(f"{'Sub-total:':<46}{items_cost_total:>16,.2f}")
print(f"{'Discount (' + str(int(discount_rate * 100)) + '%):':<46}{-discount:>16,.2f}")
print(f"{'TOTAL PURCHASE:':<46}{total_cost:>16,.2f}")
print(line)
print("Thanks for your patronage".center(62))
print(line)        
