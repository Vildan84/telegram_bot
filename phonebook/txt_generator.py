import csv


def create_txt(name="new_export"):
    bad_symbols = [",", "\\", "/", ":", "*", "?", "\"", "<", ">", "|", "+", "%", "!", " "]
    for i in bad_symbols:
        if i in name:
            return "Недопустимый символ в названии, попробуйте снова /export_contacts"
        else:
            with open('files/database.csv', newline='') as csvfile:
                txt = ""
                reader = csv.DictReader(csvfile)
                page = open(f"files/{name}.txt", 'w')
                for row in reader:
                    txt += f'Фамилия: {row["Фамилия"]}\n'
                    txt += f'Имя: {row["Имя"]}\n'
                    txt += f'Телефон: {row["Телефон"]}\n'
                    txt += f'Описание: {row["Описание"]}\n\n'
                page.write(txt)
    return "Файл экспортирован в TXT"
