def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat:
        return ""

    stock = {}

    for book in listOfArt:
        category = book[0]
        quantity = int(book.split()[1])

        stock[category] = stock.get(category, 0) + quantity

    result = []

    for category in listOfCat:
        result.append(f"({category} : {stock.get(category, 0)})")

    return " - ".join(result)