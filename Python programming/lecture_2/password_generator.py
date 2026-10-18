import random
import string

def generate_password(length: int, use_lower: bool, use_upper: bool, use_digits: bool, use_special: bool) -> str:
    char_pool = ""
    # По заданным параметрам определяем из чего генерировать пароль.
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("Необходимо выбрать хотя бы один тип символов.")

    # Гарантируем наличие как минимум одного символа из каждого выбранного типа
    password = []
    if use_lower: password.append(random.choice(string.ascii_lowercase))
    if use_upper: password.append(random.choice(string.ascii_uppercase))
    if use_digits: password.append(random.choice(string.digits))
    if use_special: password.append(random.choice(string.punctuation))

    # Заполняем оставшуюся длину случайными символами из общего пула
    while len(password) < length:
        password.append(random.choice(char_pool))

    # Перемешиваем символы, чтобы убрать предсказуемость в начале строки
    random.shuffle(password)
    
    return "".join(password[:length])


# === ПРИМЕР ВЫЗОВА ФУНКЦИИ ===
if __name__ == "__main__":
    # Параметры: длина 12 символов, включены все типы знаков
    my_password = generate_password(
        length=12, 
        use_lower=True, 
        use_upper=True, 
        use_digits=True, 
        use_special=True
    )
    
    print("Сгенерированный пароль:", my_password)
