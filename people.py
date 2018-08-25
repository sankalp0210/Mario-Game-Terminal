from time import time, sleep
import conf


class People:
    def __init__(self, x, y, Type):
        self._x = x
        self._y = y
        self._Type = Type
        self._struct = []

    def get_Type(self):
        return self._Type

    def get_coords(self):
        return (self._x, self._y)

    def update_location(self, new_x, new_y):
        self._x, self._y = new_x, new_y

    def get_struct(self):
        return self._struct


class bond(People):
    def __init__(self, x, y):
        super(bond, self).__init__(x, y, "bond")
        self._state = 1
        self.isJump = False
        self.jumpStat = 'u'
        self.make_struct()

    def make_struct(self):
        if self._state == 1:
            self._struct = conf.structBond1
        else:
            self._struct = conf.structBond2

    def get_height(self):
        return len(self._struct)

    def make_jump(self, jumpHeight=conf.jumpHeight):
        if self.isJump:
            return
        self.jumpStat = 'u'
        self.isJump = True
        self._origY = self._y
        self._incry = 0
        self._incr = conf.y_fac
        self._jumpHeight = jumpHeight

    def changeJumpDir(self):
        self.jumpStat = 'd'
        self._incr = - self._incr

    def stopJump(self):
        self.isJump = False

    def jump(self):
        self._incry += self._incr
        if self._incry > self._jumpHeight and self.isJump:
            self.jumpStat = 'd'
            self._incr = - self._incr
        y = self._origY - self._incry
        if y > conf.floor - len(self._struct) and self.isJump:
            self.isJump = False
            self.update_location(self._x, conf.floor - len(self._struct))
        else:
            self.update_location(self._x, y)

    def changeState(self, s):
        self._state += s
        self.make_struct()
        self._origY -= s

    def getState(self):
        return self._state


class Enemy(People):
    def __init__(self, x, y):
        super(Enemy, self).__init__(x, y, "enemy")
        self._struct = conf.structEnemy
        self._dir = 'L'
        self._speed = conf.enemyspeed

    def getMove(self):
        if self._dir == 'L':
            return self._speed
        else:
            return -self._speed

    def changeDir(self, dir):
        self._dir = dir

    def getDir(self):
        return self._dir


class EnemynotDie(Enemy):
    def __init__(self, x, y):
        super(EnemynotDie, self).__init__(x, y)
        self._struct = conf.structEnemynd


class Enemysmart(Enemy):
    def __init__(self, x, y):
        super(Enemysmart, self).__init__(x, y)
        self._struct = conf.structEnemysmart
        self._speed = self._speed


class Enemyboss(Enemy):
    def __init__(self, x, y):
        super(Enemyboss, self).__init__(x, y)
        self._struct = conf.structEnemyBoss


class Goli(Enemy):
    def __init__(self, x, y):
        super(Goli, self).__init__(x, y)
        self._struct = conf.structGoli
