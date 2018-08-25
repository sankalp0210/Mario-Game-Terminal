import board
import conf

inp = -1


def main():
    bd = board.Board()
    while True:
        bd.print_board()
        inp = conf.get_key(conf.get_input())
        if inp == conf.QUIT:
            break
        bd.process_input(inp)


if __name__ == '__main__':
    main()
