# Запрашиваем у пользователя два числа
num1 = float(input("Введите первое число: "))
operator = input("Введите действие (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

# Выполняем расчёт в зависимости от знака
if operator == '+':
    result = num1 + num2
    print(f"Результат: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Результат: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Результат: {result}")
elif operator == '/':
    # Проверяем, чтобы не было деления на ноль
    if num2 != 0:
        result = num1 / num2
        print(f"Результат: {result}")
    else:
        print("Ошибка: деление на ноль невозможно!")
else:
    print("Ошибка: неверная операция!")
