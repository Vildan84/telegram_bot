import os
import csv


def txt_import(filename):
    filename = "files/" + filename
    count = 0
    result = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            res = [line.strip() for line in file]
        for el in res:
            if el != "":
                result.append(el[el.index(":") + 2:])
        if len(result) % 4 != 0:
            return "Файл поврежден /start"
        else:
            for i in range(0, len(result), 4):
                adder(" ".join(res[i:i + 4]))
                count += 1
            return f"Импортировано {count} файлов /start"
    else:
        return "Указанный файл отсутствует /import_contacts"


def adder(fio):
    dic = {"Фамилия": None, "Имя": None, "Телефон": None, "Описание": None}
    list_of_adds = fio.split()

    dic["Фамилия"] = list_of_adds[0].capitalize()
    dic["Имя"] = list_of_adds[1].capitalize()
    dic["Телефон"] = list_of_adds[2].capitalize()
    dic["Описание"] = list_of_adds[3].capitalize()
    with open("files/database.csv", "a", newline="") as csvfile:
        fieldnames = ["Фамилия", "Имя", "Телефон", "Описание"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(dic)
