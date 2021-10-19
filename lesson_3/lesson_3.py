# @property
# @method.setter
# @classmethod
# @staticmethod

from datetime import datetime as dt


class Player:
    __LEVEL, __HEALTH = 1, 100
    __slots__ = ['__level', '__health', '__born']

    def __init__(self):
        self.__level = Player.__LEVEL 
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property
    def level(self):
        return self.__level,f'{dt.now() - self.__born}'

    @level.setter
    def level(self, num):
        self.__level += Player.__typeTest(num)
        if self.__level >=100: self.level = 100

    @classmethod
    def set_cls_field(cls, level=1, health=100):
        cls.__LEVEL = Player.__typeTest(level)
        cls.__HEALTH = Player.__typeTest(health)
    
    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError ('Must be int')

