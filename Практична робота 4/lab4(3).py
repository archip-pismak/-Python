# Письмак Архип Юрійович КН-45-5(13 варіант)
# Вставка нових елементів на парні позиції в списку.

def read_list_from_input(prompt: str) -> list[str]:
    #Зчитує список рядків, розділених пробілами. Коми також підтримуються як роздільники.
    raw = input(prompt).strip()
    # Дозволимо коми як роздільники: "a,b c" -> ["a","b","c"]
    parts = raw.replace(',', ' ').split()
    return parts


def insert_on_even_positions(items: list[str], new_item: str) -> list[str]:
    """Повертає новий список, де new_item вставлено на всі парні позиції (1‑базово).

    Схема формування результуючого списку (1‑базова нумерація позицій):
      позиція 1  -> оригінал[0]
      позиція 2  -> new_item
      позиція 3  -> оригінал[1]
      позиція 4  -> new_item
      ...
    Отже, вставляємо new_item після кожного елемента з індексом i, де i % 2 == 0 (0‑базово).
    """
    result: list[str] = []
    for i, val in enumerate(items):
        result.append(val)           # додаємо поточний елемент
        if i % 2 == 0:               # після 0‑го, 2‑го, 4‑го, ... вставляємо новий елемент
            result.append(new_item)
    return result


def print_list(items: list[str]) -> None:
    # Друк списку у один рядок через пробіл.
    print(' '.join(items))


def main() -> None:
    print("Операція: вставка нового елемента на парні позиції списку (1‑базово).")
    items = read_list_from_input("Введіть елементи списку через пробіл (коми дозволені): ")
    if not items:
        print("Список порожній — нічого вставляти.")
        return

    new_item = input("Введіть елемент, який потрібно вставляти на парні позиції: ").strip()
    if new_item == "":
        print("Порожній елемент вставляти не будемо.")
        return

    result = insert_on_even_positions(items, new_item)

    print("Початковий список:")
    print_list(items)
    print("Результат:")
    print_list(result)


if __name__ == "__main__":
    main()
