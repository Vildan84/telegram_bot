import xml.etree.ElementTree as et
import csv
import os


def xml_import(filename):
    filename = "files/" + filename
    if os.path.exists(filename):
        tree = et.parse(filename)
        root = tree.getroot()
        res = []
        for elem in root:
            res.append(elem.text)
        count = 0
        if len(res) % 4 != 0:
            return "Файл поврежден /start"
        else:
            for i in range(0, len(res), 4):
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