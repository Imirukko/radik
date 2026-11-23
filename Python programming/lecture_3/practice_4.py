import random

class SpaceShip:
    def __init__(self, name: str, fuel: float, hull_status: int, speed: float):
        self.name = name
        self.fuel = fuel                # В процентах или литрах
        self.hull_status = hull_status  # Прочность корпуса (0-100)
        self.speed = speed              # Текущая скорость (км/ч)

    def change_speed(self, new_speed: float):
        self.speed = new_speed
        print(f"Скорость корабля {self.name} изменена до {self.speed} км/ч.")

    def repair(self, amount: int):
        self.hull_status = min(100, self.hull_status + amount)
        print(f"Корпус корабля отремонтирован на {amount}%. Текущее состояние: {self.hull_status}%.")


class CrewMember:
    def __init__(self, name: str, role: str, health: int, skill_level: int):
        self.name = name
        self.role = role                # Например: "Пилот", "Инженер", "Медик"
        self.health = health            # Здоровье (0-100)
        self.skill_level = skill_level  # Уровень навыка (1-10)

    def take_damage(self, amount: int):
        self.health = max(0, self.health - amount)
        print(f"Член экипажа {self.name} ({self.role}) получил {amount} урона. Здоровье: {self.health}%.")


class Mission:
    def __init__(self, objective: str, duration_days: int):
        self.objective = objective
        self.duration_days = duration_days
        self.events_log = []

    def trigger_random_event(self, ship: SpaceShip, crew: list[CrewMember]):
        """Симуляция случайного события во время миссии."""
        event_type = random.choice(["asteroid", "accident", "calm"])
        
        if event_type == "asteroid":
            print("\n🚨 Внимание! Столкновение с астероидным полем!")
            ship.hull_status -= 25
            ship.fuel -= 10
            # Случайный член экипажа может пострадать
            victim = random.choice(crew)
            victim.take_damage(15)
            self.events_log.append("Столкновение с астероидом")
            
        elif event_type == "accident":
            print("\n⚠️ Произошла авария в двигательном отсеке!")
            ship.fuel -= 20
            # Ищем инженера для починки
            engineer = next((m for m in crew if m.role.lower() == "инженер"), None)
            if engineer and engineer.skill_level > 5:
                print(f"👨‍🔧 Инженер {engineer.name} успешно ликвидировал аварию с минимальными потерями!")
                ship.repair(10)
            else:
                print("💥 В экипаже нет квалифицированного инженера. Корпус поврежден!")
                ship.hull_status -= 10
            self.events_log.append("Авария в двигателе")
            
        else:
            print("\n🌌 Полет проходит в штатном режиме. Все системы стабильны.")
            ship.fuel -= 5
            self.events_log.append("Штатный полет")


# Демонстрация симуляции:
# 1. Создаем корабль и команду
my_ship = SpaceShip("Enterprise", fuel=100.0, hull_status=100, speed=28000.0)
crew_list = [
    CrewMember("Джон", "Пилот", health=100, skill_level=8),
    CrewMember("Айзек", "Инженер", health=100, skill_level=7)
]

# 2. Начинаем миссию
mars_mission = Mission(objective="Исследование Марса", duration_days=180)

# 3. Моделируем несколько дней полета
for day in range(1, 4):
    print(f"\n--- День {day} ---")
    mars_mission.trigger_random_event(my_ship, crew_list)
    if my_ship.hull_status <= 0 or my_ship.fuel <= 0:
        print("\n❌ Миссия провалена! Корабль уничтожен или остался без топлива.")
        break
else:
    print("\n✅ Первые этапы миссии успешно пройдены!")
