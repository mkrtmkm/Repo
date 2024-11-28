import os

def func():
    summ = 0

    try:
        with open("content.txt", "r", encoding="utf-8") as content:
            file_names = content.read().splitlines()

        for file_name in file_names:
            if not os.path.isfile(file_name):
                print(f"Файл '{file_name}' не існує або недоступний для читання")
                continue

            try:
                with open(file_name, "r", encoding="utf-8") as file:
                    for line in file:
                        try:
                            summ += float(line.strip())
                        except ValueError:
                            print(f"У файлі '{file_name}' містяться некоректні дані ({line.strip()})")

            except IOError:
                print(f"Неможливо прочитати файл '{file_name}'")

    except FileNotFoundError:
        print("Файл 'content.txt' не знайдено")
    except IOError:
        print("Файл 'content.txt' недоступний для читання")
    else:
        print(f"Загальна сума дійсних чисел: {summ}")
func()
