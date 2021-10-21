# Program by Sergey K.
from datetime import datetime
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\33[1;31m'



class Account:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self.history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} unit')
            self.show_balance()
            self.history.append([-amount, self._get_current_time()])

        else:
            print('Not enough money')
            self.show_balance()

    def show_balance(self):
        for amount, date in self.history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdraw'
                color = RED

            print(f'{color}  {amount} {WHITE} {transaction} on {date.astimezone()}')



a = Account('Ivan', 0)
a.deposit(100)
a.deposit(20)

a.deposit(150)
a.withdraw(75)

a.show_balance()
