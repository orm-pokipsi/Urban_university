import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                if self.balance <= 500 and self.lock.locked():
                    self.balance += amount
                    print(f'Пополнение: {amount}. Баланс: {self.balance}')
                    time.sleep(0.001)

    def take(self):
        for i in range(100):

            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонен, недостаточно средств')
                    time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
