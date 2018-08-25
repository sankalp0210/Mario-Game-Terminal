'''

contains all the symbols, constants
directions, etc

'''
# Dimensions and parameters of all the objects
height = 36
width = 600
showWidth = 120
groundSize = 6
jumpHeight = 6
floor = height - groundSize
x_fac, y_fac = (2, 2)
b = floor - 8
c1 = b - 8
springJump = 16
enemyspeed = 2
levTime = 400

# Location of different objects and enemies
bricks = [(80, b, 1), (84, b, 3), (88, b, 1), (92, b, 2), (96, b, 1), (144, b, 1), (148, b, 2), (152, b, 1), (260, b, 2), (272, b, 3), (272, c1, 2), (284, b, 2), (360, b, 2), (400,b,1), (404,b,2), (408,b,1), (412,b,2), (416,b,1), (400,c1,2), (404,c1,2), (408,c1,1), (412,c1,1), (416,c1,2), (448, b-2, 1)]
enemy = [(100, floor), (140, floor), (200, floor), (260, floor), (380, floor)]
enemynd = [(160, floor), (300, floor), (432, floor)]
enemysmart = [(400, floor)]
enemyboss = [(464, floor)]
coins = [(81, c1), (85, c1), (89, c1), (93, c1), (97, c1), (146,b-2),(148,b-2),(150,b-2),(152,b-2), (300,b), (304,b), (308,b), (312,b), (424,b), (428,b),(432,b), (440,c1)]
khai = [(220, floor), (224, floor), (328, floor), (332, floor), (336, floor), (340, floor), (344, floor)]
pipe = [(120, floor), (180, floor), (210, floor), (440, floor)]
springs = [(320, floor)]

# All the structures of mario, objects and enemies

structBond1 = [['(',')'],['/','\\']]
structBond2 = [['(',')'],['|','|'],['|','|'],['/','\\']]
structEnemy = [['E','E'],['E','E']]
structEnemynd = [['U','U'],['U','U']]
structEnemysmart = [['S','S'],['S','S']]

structBadal = []
structBadal.append([' ',' ',' ','_',',',' ','_',' ','.',' ',' ',' '])
structBadal.append([' ',' ','(',' ','(',' ','_',' ',')','_',' ',' '])
structBadal.append(['(','_','(','_',' ',' ','_','(','_',' ',',',')'])

castle = []
castle.append(list('                              |>>>                '))
castle.append(list('                              |                   '))
castle.append(list('                |>>>      _  _|_  _         |>>>  '))
castle.append(list('                |        |;| |;| |;|        |     '))
castle.append(list('            _  _|_  _    \\\\.    .  /    _  _|_  _ '))
castle.append(list('           |;|_|;|_|;|    \\\\:. ,  /    |;|_|;|_|;|'))
castle.append(list('           \\\\..      /    ||;   . |    \\\\.    .  /'))
castle.append(list('            \\\\.  ,  /     ||:  .  |     \\\\:  .  / '))
castle.append(list('             ||:   |_   _ ||_ . _ | _   _||:   |  '))
castle.append(list('             ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |  '))
castle.append(list('             ||:   ||.    .  ___.      . ||:  .|  '))
castle.append(list('             ||: . || .     /+++\ .  ,   ||:   |  '))
castle.append(list('             ||:   ||:  ,  /+++++\   .   ||: , |  '))
castle.append(list('             ||:   || .   /+++++++\    . ||:   |  '))
castle.append(list('             ||:   ||.    |+++++++| .    ||: . |  '))

structCoin = ['0']
structGoli = [['<', '<', '<', '-']]

structPipe = [['T', 'T', 'T', 'T', 'T', 'T']]
for i in range(5):
    structPipe.append(['|', '|', '|', '|', '|', '|'])

structKhai = []
for i in range(6):
    structKhai.append([' ', ' ', ' ', ' '])

structSpring = []
structSpring.append(list('\\____/'))
structSpring.append(list('/    \\'))

structEnemyBoss = []
structEnemyBoss.append(list('    |                                   '))
structEnemyBoss.append(list('    |                                   '))
structEnemyBoss.append(list(' _(9(9)__        __/^\\/^\\__             '))
structEnemyBoss.append(list('/o o   \\/_     __\\_\\_/\\_/_/_            '))
structEnemyBoss.append(list('\\___,   \\/_   _\\.\'       \'./_      _/\\_ '))
structEnemyBoss.append(list('  `---`\\  \\/_ _\\/           \\/_   _|.\'_/'))
structEnemyBoss.append(list('        \\  \\/_\\/      /      \\/_  |/ /  '))
structEnemyBoss.append(list('         \  `-\'      |        \';_:\' /   '))
structEnemyBoss.append(list('         /|          \\      \\     .\'    '))
structEnemyBoss.append(list('        /_/   |,___.-`\',    /`\'---`     '))
structEnemyBoss.append(list('         /___/`       /____/            '))

def get_structBrick(state):
    if state == 1:
        return [['[', ']', '[', ']'], ['[', ']', '[', ']']]
    elif state == 2:
        return [[' ', '?', '?', ' '], [' ', '?', '?', ' ']]
    elif state == 3:
        return [[' ', 'o', 'o', ' '], [' ', 'o', 'o', ' ']]
    elif state == 4:
        return [[' ', 'x', 'x', ' '], [' ', 'x', 'x', ' ']]

# Scores for different objects
scoreBrick1 = 10
scoreBrick2 = 200
scoreEnemy = 100
scoreEnemy2 = 100
scoreCoin = 50
scoreBossEnemy = 500

'''
    Allow certain inputs and translate to easier to read format
    UP : 0
    DOWN : 1
    LEFT : 2
    RIGHT : 3
    BOMB : 4
'''

# key presses
UP, LEFT, RIGHT, BOMB, QUIT = range(5)
DIR = [UP, LEFT, RIGHT]
INVALID = -1

# allowed inputs
_allowed_inputs = {
    UP      : ['w', '\x1b[A'], \
    LEFT    : ['a', '\x1b[D'], \
    RIGHT   : ['d', '\x1b[C'], \
    BOMB    : ['b'],           \
    QUIT    : ['q']
}

def get_key(key):
    for x in _allowed_inputs:
        if key in _allowed_inputs[x]:
            return x
    return INVALID

# Gets a single character from standard input.  Does not echo to the screen.
class _Getch:
    def __init__(self):
        self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()

class _GetchUnix:
    def __init__(self):
        pass
        # import tty, sys
    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

_getch = _Getch()

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def get_input(timeout=1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    signal.setitimer(signal.ITIMER_REAL,0.4,0.4)
    try:
        text = _getch()
        signal.alarm(0)
        signal.setitimer(signal.ITIMER_REAL,0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

# for printing colored people
colors = {
    'Black'            : '\x1b[0;30;44m',
    'Blue'             : '\x1b[0;34m',
    'Pipe'            : '\x1b[0;32;42m',
    'Boss'             : '\x1b[1;32;44m',
    'Cyan'             : '\x1b[1;36;44m',
    'Castle'           : '\x1b[2;31;44m',
    'Bond'             : '\x1b[0;31;44m',
    'Purple'           : '\x1b[0;35;44m',
    'Brown'            : '\x1b[2;33;43m',
    'Gray'             : '\x1b[0;37;44m',
    'Dark Gray'        : '\x1b[1;30m',
    'Light Blue'       : '\x1b[1;34m',
    'Light Green'      : '\x1b[1;32m',
    'Coin'             : '\x1b[1;33;44m',
    'White'            : '\x1b[1;37;44m'
}
ENDC = '\x1b[0m'
