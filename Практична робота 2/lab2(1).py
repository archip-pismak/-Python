# Письмак Архип Юрійович КН-45-5(13 варіант)
# Реалізувати дві функції користувача в одній програмі.

import math


def obchyslyty_z(x: float, y: float, u_hradusah: bool = False) -> float:
    """
    Обчислює z = cos^2(x) + sin^2(y).

    Параметри:
    - x, y: значення аргументів (радіани за замовчуванням)
    - u_hradusah: якщо True — x та y трактуються як градуси (CLI нижче завжди
      працює у радіанах і не змінює цей прапорець; параметр залишено для гнучкості).
    """
    # За потреби перетворюємо градуси у радіани, бо math.sin/cos працюють у радіанах
    if u_hradusah:
        x = math.radians(x)
        y = math.radians(y)
    # Формула з умови: z = cos^2(x) + sin^2(y)
    return math.cos(x) ** 2 + math.sin(y) ** 2

def suma_kvadrativ(n: int) -> int:
    """Повертає суму квадратів чисел від 1 до n включно.

    Для n < 1 повертає 0.
    Використовується формула n(n+1)(2n+1)/6 (закрита форма без циклів).
    Повернення робиться через цілочисельне ділення //, щоб уникнути похибок float.
    """
    if n < 1:
        return 0
    # Замкнена формула дає результат за O(1) без циклів
    return n * (n + 1) * (2 * n + 1) // 6

def _chytaty_dijsne(prompt: str) -> float:
    # Безпечне читання дійсного числа з повтором у разі помилки
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть число. Спробуйте ще раз.")

def _chytaty_natcile(prompt: str) -> int:
    # Читаємо натуральне число N (N >= 1) з валідацією вводу
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("N має бути натуральним числом (>= 1). Спробуйте ще раз.")
                continue
            return value
        except ValueError:
            print("Помилка: введіть ціле число. Спробуйте ще раз.")

if __name__ == "__main__":
    # --- Інтерактивний режим запуску ---
    print("Завдання 1: z = cos^2(x) + sin^2(y)")
    x = _chytaty_dijsne("Введіть x: ")
    y = _chytaty_dijsne("Введіть y: ")
    # Обчислюємо у радіанах (без вибору режиму)
    z = obchyslyty_z(x, y)  # обчислення за функцією
    print(f"Результат: z = {z:.6f}")

    print("\nЗавдання 2: Сума квадратів чисел від 1 до N")
    n = _chytaty_natcile("Введіть N: ")  # читання та валідація N
    s = suma_kvadrativ(n)  # обчислення суми квадратів за формулою
    print(f"Сума квадратів від 1 до {n}: S = {s}")