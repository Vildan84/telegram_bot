import csv


def search_contact_in_base(names):
    fio = names.split()
    result = ""
    if len(fio) != 2:
        return "Неверный ввод, попробуйте снова: /search_contact"
    else:
        with open("files/database.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["Фамилия"] == fio[0].capitalize() and row["Имя"] == fio[1].capitalize():
                    result += row["Фамилия"] + " " + row["Имя"] + " " + row["Телефон"] + " " + row["Описание"]
                    return result + " /start"
            else:
                return "Контакт не найден"
