import json
with open("products.json","r", encoding="utf-8") as file:
    data = json.load(file)

    for items in data["products"]:
        name = items['name']
        price = items['price']
        weight = items['weight']
        if items['available'] == True:
            available = "В наличии"
        else: available = "Нет в наличии!"

        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        print(available)
        print("")
