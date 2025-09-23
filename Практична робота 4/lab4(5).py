# Письмак Архип Юрійович КН-45-5(13 варіант)
# Задано текст з латинських літер. Символи цього тексту формують множину.Визначити та вивести всі літери, які входять у текст не менше двох разів.

from collections import Counter
import re


def read_text(prompt: str) -> str:
    # Зчитує довільний рядок від користувача
    return input(prompt)


def filter_latin_letters(text: str) -> list[str]:
    # Залишаємо тільки a-z/A-Z, перетворюємо у нижній регістр
    letters = re.findall(r"[A-Za-z]", text)
    return [ch.lower() for ch in letters]


def letters_at_least_twice_as_set(text: str) -> set[str]:
    # Обчислює множину літер, що зустрічаються не менше двох разів (без урахування регістру).
    letters_list = filter_latin_letters(text)      # маємо СПИСОК латинських літер
    counts = Counter(letters_list)                 # підрахунок появ — операція над списком
    result_list = [ch for ch, c in counts.items() if c >= 2]  # проміжний список результатів
    return set(result_list)                         # при виведенні перетворюємо на МНОЖИНУ


def print_set_as_sorted(s: set[str]) -> None:
    # Для зручності читацького сприйняття виведемо відсортовано, але як множину
    print(set(sorted(s)))


def main() -> None:
    print("Операція з множинами: вивести літери, які трапляються у тексті ≥ 2 разів (латиниця).")
    text = read_text("Введіть текст (латинські літери, інші символи ігноруються): ")

    result_set = letters_at_least_twice_as_set(text)

    if not result_set:
        print("Немає літер, що зустрічаються не менше двох разів.")
    else:
        print("Множина літер, що зустрічаються ≥ 2 разів:")
        print_set_as_sorted(result_set)


if __name__ == "__main__":
    main()

