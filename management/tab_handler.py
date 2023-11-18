from menu import products


def calculate_tab(list):
    total = 0
    for product in products:
        for item_product in list:
            if item_product["_id"] == product["_id"]:
                total += product["price"] * item_product["amount"]
            else:
                continue
    obj = {"subtotal": f"${round(total, 2)}"}

    return obj