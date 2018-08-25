import conf


class Object:
    def __init__(self, x, y, Type):
        self._x = x
        self._y = y
        self._Type = Type
        self._struct = []

    def get_Type(self):
        return self._Type

    def get_coords(self):
        return (self._x, self._y)

    def get_struct(self):
        return self._struct


class Badal(Object):
    def __init__(self, x, y):
        super(Badal, self).__init__(x, y, "Badal")
        self._struct = conf.structBadal


class Brick(Object):
    def __init__(self, x, y, state):
        super(Brick, self).__init__(x, y, "Brick")
        self._state = state
        self.make_struct()
        self._break = 1
        if self._state == 3:
            self._break = 2

    def make_struct(self):
        self._struct = conf.get_structBrick(self._state)

    def get_state(self):
        return self._state

    def update_state(self, state):
        if self._break == 0:
            self._state = state
            self.make_struct()

    def get_break(self):
        return self._break

    def Break(self):
        self._break -= 1


class Coin(Object):
    def __init__(self, x, y):
        super(Coin, self).__init__(x, y, "Coin")
        self._struct = conf.structCoin


class Khai(Object):
    def __init__(self, x, y):
        super(Khai, self).__init__(x, y, "Khai")
        x = [' ', ' ', ' ', ' ']
        self._struct = conf.structKhai


class Pipe(Object):
    def __init__(self, x, y):
        super(Pipe, self).__init__(x, y, "Pipe")
        self._struct = conf.structPipe


class Spring(Object):
    def __init__(self, x, y):
        super(Spring, self).__init__(x, y, "spring")
        self._struct = conf.structSpring


class Castle(Object):
    def __init__(self, x, y):
        super(Castle, self).__init__(x, y, "Castle")
        self._struct = conf.castle
