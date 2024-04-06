from random import*
import json


def save():
    with open("kontakts.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(kontakts,ensure_ascii=False))
    print("Ваши контакты были успешно сохранены в файле kontakts.json")

def load():
    with open("kontakts.json","r", encoding="utf-8") as fh:
        kontakts = json.load(fh)
    print("Контакты были успешно загружены! ")


kontakts = dict(мама = '96496', папа = "63463", сестра = '69438', марина = '89898', комбат = '53253')
while True:
    command = input("Введите команду: ")

    # //////////////////////////// БЛОКИ КОММАНД //////////////////////////////

    if command == "/поиск":  # Поиск номера контакта
        k = input("Введите имя контакта: ")
        print(f" Номер контакта {k} - {kontakts[k] } ")


    elif command == "/изменить": # Изменить контакт
        k = input("Выберете контакт который надо изменить: ")
        print(f"Текущий номер контакта: {kontakts[k]}")
        n = input("Введите новый номер: ")
        if n == kontakts[k]:
            print("Этот номер уже используется")
        else:
            kontakts[k] = n
            print(f"Номер контакта {k} изменён на  {kontakts[k]}")


    elif command == "/контакты":  #Показать все контакты
        print(f"Всего контактов: {len(kontakts)} ")
        for key, value in kontakts.items():
            print(f"{key} - {value}")
        
    elif command == "/добавить": #Добавить новый контакт
        Name_kontakt = input(f"Введите имя контакта: ")
        Phone_number = input(f"Введите номер контакта: ")
        kontakts[Name_kontakt] = Phone_number
        print(f"Добавлен новый контакт! ")
        print(save())

    elif command == "/удалить":
        k = input("Введите имя контакта: ")
        del kontakts[k]
        print(f"Контакт {k} удалён")

    elif command == "/сохранить":
        print(save())

    elif command == "/импорт":
        print(load())
    

        




