import json
with open("products.json","r", encoding="utf-8") as file:
    data = json.load(file)

    s = input("Хотите добавить товар в список (да/нет): ").lower()
    while s !="нет":
        name = input("Наименование товара: ")
        price = int(input("Цена: "))
        weight = int(input("Вес: "))
        available = bool(int(input("Количество товара в наличии: ")))
        new_product = {"name": name, "price": price, "available": available, "weight": weight}
        data["products"].append(new_product)
        s = input("Хотите добавить другие товары? (да/нет): ").lower()

    for items in data["products"]:
        name = items['name']
        price = items['price']
        weight = items['weight']
        if items['available']:
            available = "В наличии"
        else: available = "Нет в наличии!"
        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        print(available)
        print("")

with open("updated_products.json", "w", encoding="utf-8") as write_file:
    json.dump(data, write_file, ensure_ascii=False, indent=2)



