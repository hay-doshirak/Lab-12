data_en_ru={}
with open('en-ru.txt', "r", encoding="utf-8") as slovar:
    for line in slovar:
        if "-" in line:
            key, value = line.split("-",)
            data_en_ru[key.strip()] = value.strip()


data_ru_en = {}
for key in data_en_ru:
    if "," in data_en_ru[key]:
        translate = data_en_ru[key].split(", ")
        for i in translate:
            data_ru_en[i] = key
    else:
        data_ru_en[data_en_ru[key]] = key

data_ru_en = dict(sorted(data_ru_en.items()))

with open("ru-en.txt", "w", encoding="utf-8") as f:
    for key, value in data_ru_en.items():
        f.write(f"{key}: {value}\n")