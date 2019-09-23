from random import randint
from time import sleep


def dead_state(height, width):
    board = []
    for i in range(height):
        board.append([0] * width)
    return board


def random_state(height, width):
    board = dead_state(height, width)
    for i in range(1, height-1):
        for j in range(1, width-1):
            board[i][j] = randint(0, 1)
    return board


def render(board):
    width = len(board)
    height = len(board[0])
    # print(height,width)
    for i in range(height):
        for j in range(width):
            if board[i][j] == 1:
                print("+", end=" ")
            else:
                print(" ", end=" ")
        print(" ")


def next_board_state(board):
    width = len(board)
    height = len(board[0])
    next_board = dead_state(height, width)
    life = 0
    for i in range(1, height-1):
        for j in range(1, width-1):
            life = board[i-1][j] + board[i][j-1] + board[i-1][j-1] + board[i+1][j] + \
                board[i][j+1] + board[i+1][j+1] + \
                board[i-1][j+1] + board[i+1][j-1]
            if life <= 1:
                next_board[i][j] = 0
            elif life <= 3 and board[i][j] == 1:
                next_board[i][j] = board[i][j]
            elif life == 3 and board[i][j] == 0:
                next_board[i][j] = 1
            else:
                next_board[i][j] = 0
    return next_board


def main():
    initial = random_state(20, 20)
    render(initial)
    while True:
        next = next_board_state(initial)
        render(next)
        initial = next
        sleep(0.1)


if __name__ == "__main__":
    main()
