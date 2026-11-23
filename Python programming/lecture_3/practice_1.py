class Employee:
    def __init__(self, name: str, base_salary: float):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self) -> float:
        """Базовый расчет зарплаты (оклад)."""
        return self.base_salary


class Manager(Employee):
    def __init__(self, name: str, base_salary: float, bonus_per_project: float, projects_managed: int):
        super().__init__(name, base_salary)
        self.bonus_per_project = bonus_per_project
        self.projects_managed = projects_managed

    def calculate_salary(self) -> float:
        """Зарплата менеджера: оклад + бонусы за выполненные проекты."""
        return self.base_salary + (self.bonus_per_project * self.projects_managed)


class Developer(Employee):
    def __init__(self, name: str, base_salary: float, hourly_rate: float, overtime_hours: int):
        super().__init__(name, base_salary)
        self.hourly_rate = hourly_rate
        self.overtime_hours = overtime_hours

    def calculate_salary(self) -> float:
        """Зарплата разработчика: оклад + оплата переработок."""
        return self.base_salary + (self.hourly_rate * self.overtime_hours)


# Демонстрация работы:
emp1 = Manager("Алексей", base_salary=50000, bonus_per_project=10000, projects_managed=3)
emp2 = Developer("Иван", base_salary=70000, hourly_rate=1500, overtime_hours=10)

print(f"Зарплата менеджера {emp1.name}: {emp1.calculate_salary()} руб.")
print(f"Зарплата разработчика {emp2.name}: {emp2.calculate_salary()} руб.")
