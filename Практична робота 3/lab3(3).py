# Письмак Архип Юрійович КН-45-5 (13 варіант)
# Задано речення. Скласти програму, яка визначає і виводить на екран всі слова, які зустрічаються в реченні один раз.

from collections import Counter


def extract_words(s: str) -> list[str]:
    """
    Повертає список слів як послідовностей літер (Unicode), без цифр і розділових знаків.
    Словом вважаємо лише безперервну послідовність символів, для яких ch.isalpha() == True.
    Напр., апостроф або дефіс не включаємо до слова, бо це не літера.
    """
    words: list[str] = []
    buff: list[str] = []
    for ch in s:
        if ch.isalpha():
            buff.append(ch)
        else:
            if buff:
                words.append("".join(buff))
                buff.clear()
    if buff:
        words.append("".join(buff))
    return words


def find_unique_words(sentence: str) -> list[str]:
    # Повертає слова, що трапляються рівно один раз (реєстр нечутливий), у порядку появи, з оригінальним написанням.
    words = extract_words(sentence)
    counts = Counter(w.lower() for w in words)
    return [w for w in words if counts[w.lower()] == 1]


def main():
    sentence = input("Введіть речення: ")
    uniques = find_unique_words(sentence)
    if uniques:
        print("Слова, що зустрічаються один раз:")
        for w in uniques:
            print(w)
    else:
        print("Немає слів, що зустрічаються лише один раз.")


if __name__ == "__main__":
    main()


