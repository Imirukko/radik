def language_detect(text):
    # Автоматически определяет язык текста по буквам.
    ru_count = 0
    eng_count = 0

    for char in text.lower():
        if 'а' <= char <= 'я' or char == 'ё':
            ru_count += 1
        elif 'a' <= char <= 'z':
            eng_count += 1

    if ru_count >= eng_count and ru_count > 0:
        return "ru"
    elif eng_count > ru_count:
        return "en"
    else:
        return  "en"  # По умолчанию, если нет букв.


def ceasar_cipher(text, shift, mode='encrypt'):
    # Шифрует или дешифрует текст шифром Цезаря.
    # Если режим дешифрование, меняем знак сдвига.
    if mode == 'decrypt':
        shift = -shift

    lang = language_detect(text)

    if lang == 'ru':
        alphabet_lower = 'абвгдежзийклмнопрстуфхцчщшъыьэюя'
        alphabet_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    alphabet_size = len(alphabet_lower)
    result =[]

    for char in text:
        if char in alphabet_lower:
            old_index = alphabet_lower.index(char)
            new_index = (old_index + shift) % alphabet_size
            result.append(alphabet_lower[new_index])
        elif char in alphabet_upper:
            old_index = alphabet_upper.index(char)
            new_index = (old_index + shift) % alphabet_size
            result.append(alphabet_upper[new_index])
        else:
            # Символы пунктуации и цифры оставляем без изменений.
            result.append(char)
    return "".join(result)


print(ceasar_cipher('Всем привет я володя', 3))
print(ceasar_cipher('Ефип тулеих в есосзв', 3, mode='decrypt'))
            
