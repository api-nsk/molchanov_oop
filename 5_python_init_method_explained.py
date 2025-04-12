class Person:
    def __init__(self, name, age):
        """Инициализация объекта Person.
        
        Args:
            name (str): Имя человека.
            age (int): Возраст человека.
        """
        self.name = name  # Устанавливаем атрибут name
        self.age = age    # Устанавливаем атрибут age

    def greet(self):
        """Приветствие."""
        return f"Привет! Меня зовут {self.name}, мне {self.age} лет."

# Создаем экземпляр класса Person
person1 = Person("Алексей", 30)

# Выводим информацию
print(person1.greet())  # Вывод: Привет! Меня зовут Алексей, мне 30 лет.
print(person1.name)     # Вывод: Алексей
print(person1.age)      # Вывод: 30