class BankAccount:
    def __init__(self, owner, balance=0):
        # Публичный атрибут
        self.owner = owner
        # Приватный атрибут (используется двойное подчеркивание)
        self.__balance = balance
    
    # Публичный метод для получения баланса (геттер)
    def get_balance(self):
        return self.__balance
    
    # Публичный метод для внесения денег
    def deposit(self, amount):
        # Проверка корректности суммы
        if amount > 0:
            self.__balance += amount
            return f"Внесено {amount}. Новый баланс: {self.__balance}"
        return "Ошибка: сумма должна быть положительной"
    
    # Публичный метод для снятия денег
    def withdraw(self, amount):
        # Проверка корректности суммы и достаточности средств
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Снято {amount}. Новый баланс: {self.__balance}"
        return "Ошибка: недостаточно средств или некорректная сумма"

# Пример использования
if __name__ == "__main__":
    # Создаем объект банковского счета
    account = BankAccount("Иван", 1000)
    
    # Публичный доступ к имени владельца
    print(f"Владелец счета: {account.owner}")
    
    # Доступ к балансу через публичный метод
    print(f"Текущий баланс: {account.get_balance()}")
    
    # Внесение и снятие денег через публичные методы
    print(account.deposit(500))
    print(account.withdraw(200))
    
    # Попытка прямого доступа к приватному атрибуту вызовет ошибку
    # print(account.__balance)  # AttributeError
    
    # Попытка снять слишком большую сумму
    print(account.withdraw(2000))