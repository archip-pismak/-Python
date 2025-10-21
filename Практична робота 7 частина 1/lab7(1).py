# Письмак Архип Юрійович КН-45-5(13 варіант)
# Завдання 7. Робота з текстовими файлами.


import re

VOWELS = 'АЕЄИІЇОУЮЯаеєиіїоуюя'
FILE1 = 'TF16_1.txt'
FILE2 = 'TF16_2.txt'
 
def task_a_create_file1():
#   Створює текстовий файл TF16_1 із символьних рядків різної довжини.

    print(f"--- 1. Створення файлу {FILE1} ---")
    
    content = (
        "Осінь прийшла у наше місто. Яблука достигли!\n"
        "Це просто якийсь текст, але він має бути корисним.\n"
        "Україна - чудова країна! І ми всі її любимо.\n"
        "Еней був парубок моторний... І хлопець хоч куди козак."
    )
    
    try:
        with open(FILE1, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Файл {FILE1} успішно створено.")
        print("Його вміст:")
        print("="*20)
        print(content)
        print("="*20)
        
    except IOError as e:
        print(f"Помилка при записі у файл {FILE1}: {e}")

def task_b_process_to_file2():
    #    Читає TF16_1, знаходить слова на голосну літеру і записує кожне в окремий рядок файла TF16_2.

    print(f"\n--- 2. Обробка {FILE1} та створення {FILE2} ---")
    vowel_words = []
    

    try:
        with open(FILE1, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
        words = re.findall(r'\w+', content)
        print(f"Знайдено всі слова: {words}")
        for word in words:
            if word and word[0] in VOWELS:
                vowel_words.append(word)
        print(f"Слова, що починаються на голосну: {vowel_words}")
        with open(FILE2, 'w', encoding='utf-8') as f_out:
            for v_word in vowel_words:
                f_out.write(v_word + '\n')
        print(f"Файл {FILE2} успішно створено.")

    except FileNotFoundError:
        print(f"Помилка: Файл {FILE1} не знайдено.")
    except IOError as e:
        print(f"Помилка читання/запису: {e}")
    
    return bool(vowel_words)

def task_c_print_file2():
    # Читає вміст файла TF16_2 і друкує його по рядках.

    print(f"\n--- 3. Читання вмісту файлу {FILE2} ---")
    
    try:
        with open(FILE2, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines:
                print(f"Файл {FILE2} порожній (не знайдено слів на голосну).")
                return
            print(f"Вміст файлу {FILE2} (по рядках):")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Помилка: Файл {FILE2} не знайдено. (Можливо, крок 2 не вдався)")
    except IOError as e:
        print(f"Помилка при читанні файлу {FILE2}: {e}")

def main():
    task_a_create_file1()
    task_b_process_to_file2()
    task_c_print_file2()

if __name__ == "__main__":
    main()