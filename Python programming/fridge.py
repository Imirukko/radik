from datetime import datetime, date, timedelta
from decimal import Decimal

# Шаблон, по которому мы будем читать даты
DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    # Превращаем текстовую дату в объект даты, чтобы Python мог её сравнивать
    if expiration_date is not None:
        exp_date = datetime.strptime(expiration_date, DATE_FORMAT).date()
    else:
        exp_date = None
        
    # Переводим количество в Decimal через строку для идеальной точности расчетов
    amount_decimal = Decimal(str(amount))
    
    # Собираем данные о конкретной партии продукта в один словарь
    new_product = {'amount': amount_decimal, 'expiration_date': exp_date}
    
    # Если такого продукта еще нет в холодильнике, создаем для него пустой список партий
    if title not in items:
        items[title] = []
        
    # Добавляем новую партию в список этого продукта
    items[title].append(new_product)


def add_by_note(items, note):
    # Бьем текстовую строку на отдельные слова по пробелам
    parts = note.split()
    
    # Смотрим на самый последний элемент. Если там есть дефис — значит, это дата
    if '-' in parts[-1]:
        expiration_date = parts[-1]
        amount = parts[-2]
        title = " ".join(parts[:-2])  # Все слова до количества склеиваем обратно в название
    else:
        # Если дефиса нет — значит, даты нет, а последнее слово это количество
        expiration_date = None
        amount = parts[-1]
        title = " ".join(parts[:-1])  # Все слова до количества склеиваем в название
        
    # Вызываем нашу базовую функцию add и передаем ей очищенные данные
    add(items, title, amount, expiration_date)


def find(items, needle):
    results = []
    needle_lower = needle.lower()  # Переводим поисковый запрос в нижний регистр
    
    for title in items.keys():
        # Сравниваем слова в нижнем регистре, чтобы поиск работал независимо от больших/маленьких букв
        if needle_lower in title.lower():
            results.append(title)
            
    return results


def get_amount(items, needle):
    # Сначала находим все подходящие продукты через функцию find
    found_titles = find(items, needle)
    total_amount = Decimal('0')
    
    # Пробегаемся по всем найденным продуктам и складываем количество из всех их партий
    for title in found_titles:
        for product in items[title]:
            total_amount += product['amount']
            
    return total_amount


def get_expired(items, in_advance_days=0):
    today = date.today()
    # Вычисляем крайнюю дату проверки (сегодня + запас дней)
    target_date = today + timedelta(days=in_advance_days)
    expired_items = []
    
    for title, products_list in items.items():
        total_expired_amount = Decimal('0')
        
        # Проверяем каждую партию товара по отдельности
        for product in products_list:
            exp_date = product['expiration_date']
            # Проверяем, что срок годности есть и он уже истек или истекает к целевой дате
            if exp_date is not None and exp_date <= target_date:
                total_expired_amount += product['amount']
                
        # Если у продукта нашлись просроченные партии, добавляем его имя и вес в результат
        if total_expired_amount > 0:
            expired_items.append((title, total_expired_amount))
            
    return expired_items
