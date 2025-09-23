# Письмак Архип Юрійович КН-45-5 (13 варіант)
# Задане слово. Видалити з нього усі символи, що не є буквами.


def clean_word(s: str) -> str:
    # Повертає рядок, у якому лишилися лише літери (Unicode).
    return "".join(ch for ch in s if ch.isalpha())


def main():
    s = input("Введіть слово (можна з будь-якими символами): ")
    cleaned = clean_word(s)
    print(f"Оригінал: {s!r}")
    print(f"Тільки літери: {cleaned!r}")


if __name__ == "__main__":
    main()

