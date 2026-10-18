import random

# Список слов для игры
WORDS = ["программа", "питон", "интерфейс", "конвертер", "задача", "виселица"]

def play_hangman():
    word = random.choice(WORDS).lower()
    guessed_letters = set()  # Буквы, которые ввел игрок
    errors = 0              # Текущее количество ошибок
    max_errors = 7          # Максимальное количество ошибок по условию

    print("--- ДОБРО ПОЖАЛОВАТЬ В ИГРУ ВИСЕЛИЦА ---")

    while errors < max_errors:
        # Показываем слово (угаданные буквы открыты, остальные — "_")
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(f"\nСлово: {' '.join(display_word)}")
        print(f"Ошибок сделано: {errors} из {max_errors}")

        # Проверка на победу
        if "_" not in display_word:
            print(f" Вы выиграли! Было загадано слово: {word.upper()}")
            return

        # Ввод буквы
        guess = input("Введите одну букву: ").strip().lower()

        # Проверка ввода
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите ровно одну букву.")
            continue
            
        if guess in guessed_letters:
            print("Вы уже вводили эту букву.")
            continue

        # Запоминаем букву
        guessed_letters.add(guess)

        # Проверяем наличие буквы в слове
        if guess in word:
            print("Правильно!")
        else:
            print("Неверно! Такой буквы нет.")
            errors += 1

    # Проигрыш, если превышено число ошибок
    print(f"\n Игра окончена! Вы проиграли. Загаданное слово было: {word.upper()}")

if __name__ == "__main__":
    play_hangman()
