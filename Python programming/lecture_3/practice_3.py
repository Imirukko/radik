class Product:
    def __init__(self, name: str, price: float, stock: int, category: str):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def reduce_stock(self, quantity: int):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            raise ValueError(f"Недостаточно товара {self.name} на складе!")


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Структура: {Product: quantity}

    def add_item(self, product: Product, quantity: int = 1):
        if product.stock >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
            print(f"Добавлено в корзину: {product.name} ({quantity} шт.)")
        else:
            print(f"Невозможно добавить {product.name}, на складе всего {product.stock} шт.")

    def remove_item(self, product: Product):
        if product in self.items:
            del self.items[product]
            print(f"Удалено из корзины: {product.name}")

    def update_quantity(self, product: Product, quantity: int):
        if quantity <= 0:
            self.remove_item(product)
        elif product.stock >= quantity:
            self.items[product] = quantity
            print(f"Обновлено количество для {product.name}: {quantity} шт.")
        else:
            print(f"На складе нет такого количества товара {product.name}.")

    def get_total_items_price(self) -> float:
        return sum(prod.price * qty for prod, qty in self.items.items())


class Order:
    def __init__(self, cart: ShoppingCart, discount_pct: float = 0.0, tax_pct: float = 0.13):
        self.items = dict(cart.items)  # Копируем товары из корзины в заказ
        self.discount_pct = discount_pct  # Например, 0.10 (10%)
        self.tax_pct = tax_pct            # Например, 0.13 (13% НДС)
        self.total_price = self._process_purchase()

    def _process_purchase(self) -> float:
        # Списываем товары со склада и считаем стоимость
        base_total = 0.0
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
            base_total += product.price * quantity
        
        # Расчет с учетом скидки и налога
        with_discount = base_total * (1 - self.discount_pct)
        final_total = with_discount * (1 + self.tax_pct)
        return round(final_total, 2)


class Customer:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.order_history = []

    def checkout(self, cart: ShoppingCart, discount_pct: float = 0.0):
        if not cart.items:
            print("Корзина пуста. Нечего оформлять!")
            return
        
        new_order = Order(cart, discount_pct)
        self.order_history.append(new_order)
        cart.items.clear()  # Очищаем корзину после успешной покупки
        print(f"Заказ успешно оформлен для {self.name}. Итого к оплате: {new_order.total_price} руб.")


# Демонстрация работы магазина:
# 1. Создаем товары
phone = Product("iPhone 15", 90000, stock=5, category="Электроника")
case = Product("Чехол MagSafe", 4000, stock=20, category="Аксессуары")

# 2. Создаем покупателя и корзину
customer = Customer("Мария", "maria@mail.com")
cart = ShoppingCart()

# 3. Наполняем корзину
cart.add_item(phone, 1)
cart.add_item(case, 2)
cart.update_quantity(case, 1)  # передумали, берем 1 чехол

# 4. Оформляем покупку со скидкой 5%
customer.checkout(cart, discount_pct=0.05)
