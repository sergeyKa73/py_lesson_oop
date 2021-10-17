# объект - единица информации в пямяти
# экземпляр - конкретный объект какого то класса
# класс - инструкция по созданию объектов определенного типа
# метод - функция в классе для воздействия на объект


class Purse:
    
    def __init__(self, valute, name='Unknown') -> None:
        if valute not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.valute = valute
        self.name = name
    
    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    
    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - howmany
        return howmany


    def info(self):
        return self.__money
        

    def __del__(self):
        print('Кошелек удален')
         


x = Purse('USD')
y = Purse('USD', 'Jon')
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))

print(x.info())
print(y.info())
 