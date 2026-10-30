from datetime import datetime, date, timedelta
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if expiration_date is not None:
        exp_date = datetime.strptime(expiration_date, DATE_FORMAT).date()
    else:
        exp_date = None
      
    amount_decimal = Decimal(str(amount))
    
    new_product = {'amount': amount_decimal, 'expiration_date': exp_date}
    
    if title not in items:
        items[title] = []
        
    items[title].append(new_product)


def add_by_note(items, note):
    parts = note.split()
    
    if '-' in parts[-1]:
        expiration_date = parts[-1]
        amount = parts[-2]
        title = " ".join(parts[:-2])  
    else:
        expiration_date = None
        amount = parts[-1]
        title = " ".join(parts[:-1]) 
        
    add(items, title, amount, expiration_date)


def find(items, needle):
    results = []
    needle_lower = needle.lower()
    
    for title in items.keys():
        if needle_lower in title.lower():
            results.append(title)
            
    return results


def get_amount(items, needle):
    found_titles = find(items, needle)
    total_amount = Decimal('0')
    
    for title in found_titles:
        for product in items[title]:
            total_amount += product['amount']
            
    return total_amount


def get_expired(items, in_advance_days=0):
    today = date.today()
    target_date = today + timedelta(days=in_advance_days)
    expired_items = []
    
    for title, products_list in items.items():
        total_expired_amount = Decimal('0')
        
        for product in products_list:
            exp_date = product['expiration_date']
            if exp_date is not None and exp_date <= target_date:
                total_expired_amount += product['amount']
                
        if total_expired_amount > 0:
            expired_items.append((title, total_expired_amount))
            
    return expired_items
