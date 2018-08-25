from os import system
import sys
from conf import colors
import conf
from objects import *
from people import *
from random import randint as rand
from time import time


class Board():
    def __init__(self):
        self._height = conf.height
        self._width = conf.width
        self._showWidth = conf.showWidth
        self._lives = 3
        self.init_board()

# Function to initialise all the elements of the game.
    def init_board(self):

        self._loc = 0
        self._score = 0
        self._ncoin = 0
        self._board = []
        self._leftTime = conf.levTime
        self._startTime = time()
        for i in range(self._height):
            x = []
            for j in range(self._width):
                x.append(' White')
            self._board.append(x)
        self.init_badals()
        self.init_bond()
        self.init_bricks()
        self.init_enemies()
        self.init_enemynd()
        self.init_enemysmart()
        self.init_coins()
        self.init_khai()
        self.init_pipe()
        self.init_spring()
        self.init_enemyboss()
        self.init_castle()

    def print_floor(self):
        b = []
        for j in range(int(self._width/2)):
            b.append('[Brown')
            b.append(']Brown') 
        
        for i in range(self._height-6,self._height):
            self._board[i] = b
        
    def init_badals(self):
        x = 6
        self._badal = []
        while x < self._width - int(self._showWidth/2):
            x += rand(5,int(self._showWidth/4))
            y = rand(0,1)
            ba = Badal(x,y)
            self._badal.append(ba)

    def init_bond(self):
        self._bond = bond(int(self._showWidth/4),conf.floor - 2)

    def print_bond(self):
        struct = self._bond.get_struct()
        x, y = self._bond.get_coords()
        for j in range(len(struct)):
            for k in range(len(struct[j])):
                try:
                    self._board[y+j][x+k] = struct[j][k] + 'Bond'
                except:
                    pass
    def print_castle(self):
        struct = self._castle.get_struct()
        x, y = self._castle.get_coords()
        for j in range(len(struct)):
            for k in range(len(struct[j])):
                try:
                    self._board[y+j][x+k] = struct[j][k] + 'Castle'
                except:
                    pass
    def init_pipe(self):
        self._pipe = []
        for i in conf.pipe:
            x, y = i
            pipe = Pipe(x, y - len(conf.structPipe))
            self._pipe.append(pipe)
    
    def init_khai(self):
        self._khai = []
        for i in conf.khai:
            x, y = i
            khai = Khai(x,y)
            self._khai.append(khai)
    
    def init_enemies(self):
        self._enemies = []
        for i in conf.enemy:
            x, y = i
            enemy = Enemy(x,y-2)
            self._enemies.append(enemy)

    def init_enemynd(self):
        self._enemynd = []
        for i in conf.enemynd:
            x, y = i
            enemy = EnemynotDie(x,y-2)
            self._enemynd.append(enemy)
    
    def init_enemysmart(self):
        self._enemysmart = []
        for i in conf.enemysmart:
            x, y = i
            enemy = Enemysmart(x,y-2)
            self._enemysmart.append(enemy)

    def init_enemyboss(self):
        self._enemyboss = []
        self._bossGoli = []
        for i in conf.enemyboss:
            x, y = i
            enemy = Enemyboss(x,y-len(conf.structEnemyBoss))
            self._enemyboss.append(enemy)

    def init_castle(self):
        self._castle = Castle(self._width-int(self._showWidth/2),conf.floor-len(conf.castle))

    def print_objects(self,element,col):
        for i in element:
            ele = i.get_struct()
            x, y = i.get_coords()
            for j in range(len(ele)):
                for k in range(len(ele[j])):
                    try:
                        self._board[y+j][x+k] = ele[j][k] + col
                    except:
                        pass

# To move enemies on the screen. 
    def moveEnemies(self):
        for i in range(len(self._enemies)-1,-1,-1):
            x, y = self._enemies[i].get_coords()
            if x in range(self._loc,self._loc+self._showWidth):
                self._enemies[i].update_location(x-self._enemies[i].getMove(),y)
            if x < self._loc:
                del self._enemies[i]

    def moveEnemynd(self):
        for i in range(len(self._enemynd)-1,-1,-1):
            x, y = self._enemynd[i].get_coords()
            if x in range(self._loc,self._loc+self._showWidth):
                self._enemynd[i].update_location(x-self._enemynd[i].getMove(),y)
            if x < self._loc:
                del self._enemynd[i]

    def moveEnemyboss(self):
        x1, y1 = self._bond.get_coords()
        for i in self._enemyboss:
            x, y = i.get_coords()
            if x in range(x1-6,x1+40) and rand(0,10) == 0:
                y = conf.floor - len(conf.structEnemyBoss) - rand(0,5)
                i.update_location(x,y)
                k = y + len(conf.structEnemyBoss) -1
                y2 = rand(y,k)
                self._bossGoli.append(Goli(x-len(conf.structGoli),y2))
    
    def moveGoli(self):
        for i in self._bossGoli:
            x, y = i.get_coords()
            i.update_location(x-2,y)

    def moveEnemysmart(self):
        x1, y1 = self._bond.get_coords()
        for i in range(len(self._enemysmart)-1,-1,-1):
            x, y = self._enemysmart[i].get_coords()
            dir = self._enemysmart[i].getDir()
            if x in range(x1-6,x1+40) and dir == 'L':
                self._enemysmart[i].update_location(x-self._enemysmart[i].getMove(),y)
            elif x > x1 + 6:
                self._enemysmart[i].changeDir('L')
            elif x in range(x1-20,x1+8) and dir == 'R':
                self._enemysmart[i].update_location(x - self._enemysmart[i].getMove(),y)
            elif x < x1 - 6:
                self._enemysmart[i].changeDir('R')
    
    def init_coins(self):
        self._coins = []
        for i in conf.coins:
            x, y = i
            coin = Coin(x,y)
            self._coins.append(coin)

    def init_bricks(self):
        self._bricks = []
        for i in conf.bricks:
            x, y, s = i
            brick = Brick(x,y,s)
            self._bricks.append(brick)
    
    def init_spring(self):
        self._springs = []
        for i in conf.springs:
            x, y = i
            spring = Spring(x,y - len(conf.structSpring))
            self._springs.append(spring)
    

    def updateTime(self):
        self._leftTime = conf.levTime - int(time() - self._startTime)
# Processing the input
    def process_input(self,key_press):
        self.moveEnemies()
        self.moveEnemynd()
        self.moveEnemysmart()
        self.moveEnemyboss()
        self.moveGoli()
        
        if self._bond.isJump == True:
            x, y = self._bond.get_coords()
            self._bond.jump()

        if key_press in conf.DIR:
            x, y = self._bond.get_coords()
            if key_press == conf.LEFT:
                if x in range(self._loc+4, self._loc + self._showWidth):
                    x -= conf.x_fac

            elif key_press==conf.RIGHT:
                if x > self._loc + int(self._showWidth/2):
                    if self._loc < self._width - self._showWidth:
                        self._loc += conf.x_fac
                    if x < self._width - 10:
                        x += conf.x_fac
                else:
                    x += conf.x_fac
            
            elif key_press == conf.UP:
                x, y = self._bond.get_coords()
                if x == 448:
                    self._bond.make_jump(12)
                self._bond.make_jump()
            self._bond.update_location(x,y)

        self.checkCollisionEnemies()
        self.checkCollisionEnemynd()
        self.checkCollisionEnemysmart()
        self.checkCollisionBossGoli()
        self.checkCollisionEnemyboss()
        self.checkCollisionBrick()
        self.checkCollisionCoins()
        self.checkCollisionKhai()
        self.checkCollisionPipe()
        self.checkCollisionSpring()
        self.checkCollisionEnemyPipe()
        self.checkCollisionEnemyKhai()
        self.checkCollisionEnemyndPipe()
        self.checkCollisionEnemysmartPipe()

# Checking collisions with all the objects.
    def checkCollisionBrick(self):
        x, y = self._bond.get_coords()
        h = self._bond.get_height()
        if self._board[y+h][x] == ' White' and self._bond.isJump == False:
            self._bond.make_jump()
            self._bond.changeJumpDir()
        for i in range(len(self._bricks)):
            x1, y1 = self._bricks[i].get_coords()
            s = self._bricks[i].get_state()
            if x1 in range(x-2,x+1) and ((y1==y-h and self._bond.getState()==1) or\
             y1 ==y and self._bond.getState()==2) and self._bond.jumpStat=='u':
                self._bond.changeJumpDir()
                self._bricks[i].Break()
                if s == 1:
                    self._score += conf.scoreBrick1
                    del self._bricks[i]
                elif s == 2:
                    self._bond.update_location(x,y1+2)
                    self._ncoin += 10
                    self._score += conf.scoreBrick2
                    self._bricks[i].update_state(4)
                elif s == 3 and self._bricks[i].get_break()==0:
                    self._bricks[i].update_state(4)
                    self._bond.changeState(1)
                    del self._bricks[i]
                break
            elif (x1==x or x1==x-2) and ((y1==y and self._bond.getState()==1) or\
             (y1==y+2) and self._bond.getState()==2) and self._bond.jumpStat=='d':
                self._bond.update_location(x,y1-h)
                self._bond.stopJump()

    def checkCollisionEnemies(self):
        x, y = self._bond.get_coords()
        h = self._bond.get_height()
        for i in range(len(self._enemies)):
            x1, y1 = self._enemies[i].get_coords()
            if (x1 in range(x-2,x+2)) and ((y1==y and self._bond.getState() ==1)or\
             (y1 in range(y,y+4) and self._bond.getState()==2)):
                if x1 >= x-1:
                    self._enemies[i].update_location(x+2,y1)
                else:
                    self._enemies[i].update_location(x-2,y1)
                self.respawn()
            elif (x1 == x or x1 == x+2) and y1 in range(y+1,y+h+1) and self._bond.jumpStat=='d':
                self._score += conf.scoreEnemy
                del self._enemies[i]
                break

    def checkCollisionEnemysmart(self):
        x, y = self._bond.get_coords()
        h = self._bond.get_height()
        for i in range(len(self._enemysmart)):
            x1, y1 = self._enemysmart[i].get_coords()
            if (x1 in range(x-2,x+2)) and ((y1==y and self._bond.getState() ==1)or\
             (y1 in range(y,y+4) and self._bond.getState()==2)):
                if x1 >= x-1:
                    self._enemysmart[i].update_location(x+2,y1)
                else:
                    self._enemysmart[i].update_location(x-2,y1)
                self.respawn()
            elif (x1 == x or x1 == x+2) and y1 in range(y+1,y+h+1) and self._bond.jumpStat=='d':
                self._score += conf.scoreEnemy2
                del self._enemysmart[i]
                break

    def checkCollisionEnemyboss(self):
        x, y = self._bond.get_coords()
        h = self._bond.get_height()
        for i in range(len(self._enemyboss)):
            x1, y1 = self._enemyboss[i].get_coords()
            l=len(conf.structEnemyBoss[0])
            h1=len(conf.structEnemyBoss)
            if x in range(x1,x1+l) and y in range(y1,y1+h1):
                self.respawn()
            elif x in range(x1,x1+l) and y in range (y1-2,y1) and self._bond.jumpStat=='d':
                self._score += conf.scoreBossEnemy
                del self._enemyboss[i]
                break
    def checkCollisionBossGoli(self):
        x, y = self._bond.get_coords()
        h = self._bond.get_height()
        for i in self._bossGoli:
            x1, y1 = i.get_coords()
            l=len(conf.structGoli)
            if x in range(x1-1,x1+l) and y1 in range(y-1,y+2):
                self.respawn()

    def checkCollisionEnemynd(self):
        x, y = self._bond.get_coords()
        # h = self._bond.get_height()
        for i in range(len(self._enemynd)):
            x1, y1 = self._enemynd[i].get_coords()
            if(x1 in range(x-2,x+2))and((y1==y and self._bond.getState()==1)or\
             (y1 in range(y,y+4) and self._bond.getState()==2)):
                if x1 >= x-1:
                    self._enemynd[i].update_location(x+2,y1)
                else:
                    self._enemynd[i].update_location(x-2,y1)
                self.respawn()
                break

    def checkCollisionKhai(self):
        x, y = self._bond.get_coords()
        h = self._bond.get_height()
        for i in range(len(self._khai)):
            x1, y1 = self._khai[i].get_coords()
            if x in range(x1,x1+len(conf.structKhai[0])) and y1 == y + h:
                self._bond.update_location(x,y)
                self.respawn()

    def checkCollisionSpring(self):
        x, y = self._bond.get_coords()
        h = self._bond.get_height()
        for i in range(len(self._springs)):
            x1, y1 = self._springs[i].get_coords()
            if x in range(x1,x1+len(conf.structSpring[0])) and y1 in range(y+1,y+h+1):
                self._bond.update_location(x,y1-h)
                self._bond.stopJump()
                self._bond.make_jump(conf.springJump)

    def checkCollisionEnemyKhai(self):
        for j in range(len(self._khai)):
            x1, y1 = self._khai[j].get_coords()
            for i in range(len(self._enemies)):
                x, y = self._enemies[i].get_coords()
                if x in range(x1,x1+len(conf.structKhai[0])) and y1 == y + 2:
                    del self._enemies[i]
                    break

    def checkCollisionPipe(self):
        x, y = self._bond.get_coords()
        h = self._bond.get_height()
        for i in range(len(self._pipe)):
            x1, y1 = self._pipe[i].get_coords()
            l = len(conf.structPipe[0])
            if x in range(x1-1,x1+l+1) and (y1==y or y1 == y+2) and self._bond.jumpStat=='d':
                self._bond.update_location(x,y1-h)
                self._bond.stopJump()
            elif x in range(x1,x1+l-2) and y + h> y1:
                self._bond.update_location(x1-2,y)
            elif x in range(x1+l-2,x1+l) and y + h>y1:
                self._bond.update_location(x1+l,y)

    def checkCollisionEnemyPipe(self):
        for i in self._pipe:
            l = len(conf.structPipe[0])
            x, y = i.get_coords()
            for j in self._enemies:
                x1, y1 = j.get_coords()
                if x == x1 + 2:
                    j.changeDir('L')
                elif x + l == x1:
                    j.changeDir('R')

    def checkCollisionEnemyndPipe(self):
        for i in self._pipe:
            l = len(conf.structPipe[0])
            x, y = i.get_coords()
            for j in self._enemynd:
                x1, y1 = j.get_coords()
                if x == x1 + 2:
                    j.changeDir('L')
                elif x + l == x1:
                    j.changeDir('R')

    def checkCollisionEnemysmartPipe(self):
        for i in self._pipe:
            l = len(conf.structPipe[0])
            x, y = i.get_coords()
            for j in self._enemysmart:
                x1, y1 = j.get_coords()
                if x == x1 + 2:
                    j.changeDir('L')
                elif x + l == x1:
                    j.changeDir('R')
                    
    def checkCollisionCoins(self):
        x, y = self._bond.get_coords()
        h = self._bond.get_height()
        for i in range(len(self._coins)):
            x1, y1 = self._coins[i].get_coords()
            if (x1 == x or x1 == x+1) and y1 in range(y,y+h):
                self._score += conf.scoreCoin
                self._ncoin += 1
                del self._coins[i]
                break
# clearing the board to empty
    def clearBoard(self):
        for i in range(self._height):
            for j in range(self._width):
                self._board[i][j] = ' White'

    def print_board(self):
        self.updateTime()
        self.checkEndGame()
        self.clearBoard()
        self.print_floor()
        self.print_objects(self._bricks,'Brown')
        self.print_objects(self._khai,'White')
        self.print_objects(self._badal,'White')
        self.print_objects(self._coins,'Coin')
        self.print_objects(self._pipe,'Pipe')
        self.print_objects(self._springs,'White')
        self.print_objects(self._bossGoli,'Black')
        self.print_objects(self._enemies,'Gray')
        self.print_objects(self._enemynd,'Cyan')
        self.print_objects(self._enemysmart,'Black')
        self.print_objects(self._enemyboss,'Boss')
        self.print_castle()
        self.print_bond()
        self.printBoard()

    def printBoard(self):
        system('clear')
        print('Mario           Lives:',self._lives,end = '')
        print('           Score:',self._score,end = '')
        print('           Coins:',self._ncoin,end = '')
        print('           Time:',self._leftTime)
        for i in self._board:
            for j in i[self._loc:self._showWidth+self._loc]:
                print(colors[j[1:]]+j[0] + conf.ENDC,end='')
            print('')

    def checkEndGame(self):
        x, y =  self._bond.get_coords()
        if x >= self._width - int(self._showWidth/2):
            self._score += self._leftTime*10
            self.printBoard()
            self.endGame("You Won")

    def endGame(self,str):
            print('')
            print('   ',str,' !!!!!   Score : ',self._score,'    Coins:',self._ncoin)
            print('')
            quit()

# deleting all the elements of the board
    def delBoard(self):
        del self._bond
        for i in range(len(self._enemies)-1,-1,-1):
            del self._enemies[i]
        for i in range(len(self._bricks)-1,-1,-1):
            del self._bricks[i]
        for i in range(len(self._badal)-1,-1,-1):
            del self._badal[i]
        for i in range(len(self._coins)-1,-1,-1):
            del self._coins[i]
        del self._board

# To spawn the mario after dying.
    def respawn(self):
        system('clear')
        self.print_board()
        sleep(1)
        if self._lives == 1:
            self.endGame("Game Over")    
        self._lives -= 1
        system('clear')
        self.delBoard()
        self.init_board()
