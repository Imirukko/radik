def print_pack_report(pie_amount):
    # Перебираем все числа от заданного до 1 включительно, в порядке убывания.
    for num in range(pie_amount, 0, -1):
        if num % 5 == 0 and num % 3 == 0:
            print(f"{num} - расфасуем по 3 или по 5")
        elif num % 5 == 0:
            print(f"{num} - расфасуем по 5")
        elif num % 3 == 0:
            print(f"{num} - расфасуем по 3")
        else:
            print(f"{num} - не заказываем!")

print_pack_report(12)