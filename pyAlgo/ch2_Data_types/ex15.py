#Safely Convert Order Rows

orders = [
    {"sku": "A100", "price": "12.50", "quantity": "4"},
    {"sku": "B200", "price": "free", "quantity": "2"},
    {"sku": "C300", "price": "7.25", "quantity": "3.0"},
    {"sku": "D400", "price": " 5.00 ", "quantity": " 6 "},
]


def order_total(row):
    # TODO: convert row["price"] with float() and row["quantity"] with int().
    # TODO: return "INVALID" if either conversion raises ValueError
    try:
        price = float(row["price"])
        quantity = int(row["quantity"])
    except ValueError:
        return "INVALID"

    return f"${price * quantity:.2f}"


for order in orders:
    print(f"{order['sku']}: {order_total(order)}")