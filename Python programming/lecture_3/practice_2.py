class Vehicle:
    def __init__(self, model: str):
        self.model = model

    def get_description(self) -> str:
        return f"Это неопределенное транспортное средство модели {self.model}."


class Car(Vehicle):
    def get_description(self) -> str:
        return f"Автомобиль {self.model}: передвигается по дорогам общего пользования на 4 колесах."


class Bicycle(Vehicle):
    def get_description(self) -> str:
        return f"Велосипед {self.model}: экологичный двухколесный транспорт, приводимый в движение силой мышц."


class Airplane(Vehicle):
    def get_description(self) -> str:
        return f"Самолет {self.model}: воздушное судно для дальних перелетов на высокой скорости."


# Демонстрация полиморфизма:
fleet = [
    Car("Tesla Model 3"),
    Bicycle("Giant Talon"),
    Airplane("Boeing 737")
]

# Один и тот же вызов метода возвращает разное поведение для каждого объекта
for vehicle in fleet:
    print(vehicle.get_description())
