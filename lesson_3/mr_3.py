from lesson_3 import Player

Player.set_cls_field(10)
x = Player()
print(x.level)

x.set_cls_field()
y = Player()
print(y.level)
y.level = 2.3
