def int_to_roman(num: int) -> str:
    # Базовые пары чисел и соответствующих им римских букв
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_num = ""
    i = 0
    
    # Жадный алгоритм: вычитаем максимально возможные числа из списка val
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
        
    return roman_num


def roman_to_int(roman: str) -> int:
    # Словарь соответствия римских символов и их числовых значений
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0
    
    # Обход строки в обратном направлении (справа налево)
    for char in reversed(roman):
        value = roman_map[char]
        
        # Правило вычитания: если текущая цифра меньше предыдущей (идущей после неё)
        if value < prev_value:
            total -= value
        else:
            total += value
            
        prev_value = value
        
    return total
