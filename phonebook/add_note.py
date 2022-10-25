from tel_checker import check_tel
import csv


def add_note_to_base(fio):
    dic = {"Фамилия": None, "Имя": None, "Телефон": None, "Описание": None}
    list_of_adds = fio.split()
    if len(list_of_adds) != 4:
        return "Введите фамилию, имя, телефон и описание через пробел /add_contact"
    else:
        dic["Фамилия"] = list_of_adds[0].capitalize()
        dic["Имя"] = list_of_adds[1].capitalize()
        if not check_tel(list_of_adds[2]):
            return "Не правильно введен номер, попробуйте ввести все заново /add_contact"
        else:
            dic["Телефон"] = check_tel(list_of_adds[2])
        dic["Описание"] = list_of_adds[3].capitalize()
    with open("files/database.csv", "a", newline="") as csvfile:
        fieldnames = ["Фамилия", "Имя", "Телефон", "Описание"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(dic)
    return "Контакт добавлен!!! Нажмите: /start"
