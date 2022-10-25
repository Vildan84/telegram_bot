import csv


def create_xml(name="new_export"):
    bad_symbols = [",", "\\", "/", ":", "*", "?", "\"", "<", ">", "|", "+", "%", "!", " "]
    for i in bad_symbols:
        if i in name:
            return "Недопустимый символ в названии, попробуйте снова /export_contacts"
        else:
            xml = '<xml>\n'
            with open("files/database.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    xml += f'<Фамилия>{row["Фамилия"]}</Фамилия>\n'
                    xml += f'<Имя>{row["Имя"]}</Имя>\n'
                    xml += f'<Телефон>{row["Телефон"]}</Телефон>\n'
                    xml += f'<Описание>{row["Описание"]}</Описание>\n'
            xml += '</xml>'
            with open(f"files/{name}.xml", 'w') as page:
                page.write(xml)
    return "Файл экспортирован в XML"
