import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Угадай число (1-100): "))
    attempts += 1
    if guess < secret:
        print("Больше!")
    elif guess > secret:
        print("Меньше!")
    else:
        print(f"Верно! Попыток: {attempts}")
        break
