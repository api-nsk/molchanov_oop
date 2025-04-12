from datetime import datetime, timezone
from decimal import Decimal
from typing import List, Tuple

# Константы для цветов
class Colors:
    WHITE = "\033[00m"
    GREEN = "\033[0;92m"
    RED = "\033[1;31m"

class Transaction:
    """Класс для хранения информации о транзакции"""
    def __init__(self, amount: Decimal, timestamp: str, type: str):
        self.amount = amount
        self.timestamp = timestamp
        self.type = type

class Account:
    def __init__(self, name: str, balance: float = 0.0):
        self.name = name
        self.balance = Decimal(str(balance))  # Используем Decimal для точных расчетов
        self._history: List[Transaction] = []
        
    def deposit(self, amount: float) -> bool:
        """Пополнение счета"""
        try:
            amount = Decimal(str(amount))
            if amount <= 0:
                raise ValueError("Amount must be positive")
                
            self.balance += amount
            self._history.append(Transaction(
                amount,
                datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                "deposit"
            ))
            self._show_balance()
            return True
            
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
            return False

    def withdraw(self, amount: float) -> bool:
        """Снятие со счета"""
        try:
            amount = Decimal(str(amount))
            if amount <= 0:
                raise ValueError("Amount must be positive")
                
            if self.balance >= amount:
                self.balance -= amount
                self._history.append(Transaction(
                    -amount,
                    datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    "withdraw"
                ))
                print(f"You spent {amount} units")
                self._show_balance()
                return True
            else:
                print("Not enough money")
                self._show_balance()
                return False
                
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
            return False

    def _show_balance(self) -> None:
        """Отображение текущего баланса"""
        print(f"Balance: {self.balance:.2f}")

    def show_history(self) -> None:
        """Отображение истории транзакций"""
        if not self._history:
            print("No transactions yet")
            return
            
        print(f"\nTransaction history for {self.name}:")
        for transaction in self._history:
            color = Colors.GREEN if transaction.type == "deposit" else Colors.RED
            amount = abs(transaction.amount)  # Показываем положительное значение
            print(f"{color}{amount:.2f} {Colors.WHITE}{transaction.type} on {transaction.timestamp}")

    def get_balance(self) -> Decimal:
        """Получение текущего баланса"""
        return self.balance

if __name__ == "__main__":
    # Пример использования
    account = Account("Petr", 0)
    account.deposit(100.50)
    account.withdraw(30.25)
    account.deposit(200)
    account.withdraw(300)  # Ошибка: недостаточно средств
    account.show_history()