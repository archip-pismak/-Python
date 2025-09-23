# Письмак Архип Юрійович КН-45-5(13 варіант)
# Заповнити двовимірний масив 7x7 згідно рисунку.

ROWS = 7
COLS = 7


def value_for_position(i: int, j: int) -> int:
    # Тут легко змінити під конкретний зразок.
    return 1 if i % 2 == 0 else 0


def build_matrix(rows: int, cols: int) -> list[list[int]]:
    # Створює матрицю розміром rows x cols згідно правила value_for_position.

    matrix: list[list[int]] = []
    for i in range(rows):  # зовнішній цикл за рядками
        row: list[int] = []
        for j in range(cols):  # внутрішній цикл за стовпцями
            row.append(value_for_position(i, j))
        matrix.append(row)
    return matrix


def print_matrix(matrix: list[list[int]]) -> None:
    # Друкує матрицю у зручному для читання вигляді.
    for row in matrix:
        # Вивід через пробіл без ком
        print(" ".join(str(x) for x in row))


def main():
    matrix = build_matrix(ROWS, COLS)
    print_matrix(matrix)


if __name__ == "__main__":
    main()

