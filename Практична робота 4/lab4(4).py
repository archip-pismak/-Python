# Письмак Архип Юрійович КН-45-5(13 варіант)
# Поміняти місцями елементи списку з парними і непарними індексами.


def read_list_from_input(prompt: str) -> list[str]:
    # Зчитує список рядків, розділених пробілами. Коми також підтримуються як роздільники.
    raw = input(prompt).strip()
    parts = raw.replace(',', ' ').split()
    return parts


def swap_even_odd_indices(items: list[str]) -> list[str]:
    # Повертає новий список, де елементи з парними і непарними індексами поміняні місцями попарно.
    res = items.copy()
    # Ітеруємося по парних індексах (0, 2, 4, ...), міняючи місцями i та i+1, якщо він існує
    for i in range(0, len(res) - 1, 2):
        res[i], res[i + 1] = res[i + 1], res[i]
    return res


def print_list(items: list[str]) -> None:
    # Друк списку у один рядок через пробіл.
    print(' '.join(items))


def main() -> None:
    print("Операція: поміняти місцями елементи списку з парними і непарними індексами.")
    items = read_list_from_input("Введіть елементи списку через пробіл (коми дозволені): ")
    if not items:
        print("Список порожній — нічого міняти.")
        return

    result = swap_even_odd_indices(items)

    print("Початковий список:")
    print_list(items)
    print("Результат:")
    print_list(result)


if __name__ == "__main__":
    main()

