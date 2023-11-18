from menu import products


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    return next((product for product in products if id == product["_id"]), {})


def get_products_by_type(type_product: str):
    if type(type_product) != str:
        raise TypeError("product type must be a str")
    list_products = []
    for product in products:
        if product["type"] == type_product:
            list_products.append(product)
            continue
        else:
            continue
    return list_products


def add_product(list: list, **prod):
    add_id = 0
    for product in list:
        if product["_id"] > add_id:
            add_id = product["_id"]
            continue
        else:
            continue

    id = 1
    if add_id != 0:
        id = add_id + 1

    prod["_id"] = id

    list.append(prod)

    return prod


def menu_report():
    product_count = len(products)

    price = 0
    for product in products:
        price += product["price"]
    average_price = round((price / product_count), 2)

    common_type = products[0]["type"]
    for product in products:
        if products.count(product["type"]) > products.count(common_type):
            common_type = product["type"]

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {common_type}"