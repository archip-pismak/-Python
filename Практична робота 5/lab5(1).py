# Письмак Архип Юрійович КН-45-5(13 варіант)
# Робота зі словником


# Словник оцінок учнів
students = {
    "Vitaly_Prikhodko": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10],
    "Dmytro_Kropyvnytskyi": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4],
    "Mikhail_Romanenko": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4],
    "Maxim_Derizemlya": [12, 4, 10, 7, 5, 8, 3, 3, 5, 7],
    "Victoria_Zhuk": [10, 10, 10, 9, 10, 9, 10, 8, 7, 12],
    "Andrey_Kuryanov": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8],
    "Oksana_Dubovets": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10],
    "Nikita_Stroganov": [6, 7, 8, 9, 10, 10, 10, 10, 10, 9],
    "Karina_Nikolaenko": [2, 3, 5, 4, 5, 4, 3, 3, 5, 8],
    "Eugenia_Dron": [12, 12, 12, 10, 10, 9, 8, 9, 9, 8]
}

# Функція виведення словника
def Print(students):
    for i in students:
        print("Оцінки", i, "-", students[i])

# Функція додавання запису
def add(students, key, grades):
    students[key] = grades
    print("Додано", key)

# Функція видалення запису
def Del(students, key):
    if key in students:
        del students[key]
        print("Видалено", key)
    else:
        print("Запису", key, "не існує!")

# Функція сортування словника за ключами
def print_sort(students):
    sorted_students = {k: students[k] for k in sorted(students)}
    print("Відсортований словник:")
    for i in sorted_students:
        print("Оцінки", i, "-", sorted_students[i])

# Функція для учня з найбільшою сумою оцінок
def max_sum(students):
    key = max(students, key=lambda k: sum(students[k]))
    print("Учень з найбільшою сумою оцінок:", key, "-", students[key], "Сума:", sum(students[key]))

# Функція для учня з найменшою сумою оцінок
def min_sum(students):
    key = min(students, key=lambda k: sum(students[k]))
    print("Учень з найменшою сумою оцінок:", key, "-", students[key], "Сума:", sum(students[key]))

# Меню взаємодії
def menu():
    while True:
        print("\nМеню:")
        print("1 - Вивести всі оцінки")
        print("2 - Додати запис")
        print("3 - Видалити запис")
        print("4 - Відсортувати словник")
        print("5 - Учень з найбільшою сумою оцінок")
        print("6 - Учень з найменшою сумою оцінок")
        print("0 - Вихід")
        choice = input("Введіть пункт меню: ")
        
        if choice == "1":
            Print(students)
        elif choice == "2":
            key = input("Введіть прізвище та ім'я учня: ")
            try:
                grades = list(map(int, input("Введіть оцінки через пробіл: ").split()))
                add(students, key, grades)
            except ValueError:
                print("Некоректний формат оцінок!")
        elif choice == "3":
            key = input("Введіть прізвище та ім'я учня для видалення: ")
            Del(students, key)
        elif choice == "4":
            print_sort(students)
        elif choice == "5":
            max_sum(students)
        elif choice == "6":
            min_sum(students)
        elif choice == "0":
            print("Вихід з програми")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")

# Запуск меню
menu()
