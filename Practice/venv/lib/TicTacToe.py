# Tic-Tac-Toe Game. First Milestone Project

from collections import deque

def player_input():

    marker = input("Player 1 chooses marker either X or O: ")

    while marker != 'X' and marker != 'O':
        marker = input("Player 1 chooses marker either X or O: ")

    player1 = marker
    if marker == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

def display_board(boardList):
    print(str(boardList[0]) + "  | " + str(boardList[1]) + "  | " + str(boardList[2]))
    print("----------")
    print(str(boardList[3]) + "  | " + str(boardList[4]) + "  | " + str(boardList[5]))
    print("----------")
    print(str(boardList[6]) + "  | " + str(boardList[7]) + "  | " + str(boardList[8]))

def populateEmptyBoard(boardList):

    for index in range(9):
        print("index: " + str(index))
        boardList.popleft()
        boardList.append(index + 1)
    return boardList

def startGame(board, firstTurn):
    winner = None
    turn = firstTurn

    while winner is None:
        numInput = input("choose slot: ")
        if not range(0, 9):
            print("Invalid Input, please retry again: ")
            continue

        if board[int(numInput) - 1] == int(numInput):
            board[int(numInput) - 1] = turn
            if turn == "X":
                turn = "O"
            else:
                turn = "X"

            display_board(board)
            winner = checkWinner(board)
        else:
            print("Slot is already taken; please choose another slot")
            continue

    if winner == "draw":
        print("The game is draw!")
    else:
        print("Congrats Player with " + winner + " is winner.")

def checkWinner(board):

    for a in range(8):
        winner = ""

        if a == 0:
            winner = str(board[0]) + str(board[1]) + str(board[2])
        elif a == 1:
            winner = str(board[3]) + str(board[4]) + str(board[5])
        elif a == 2:
            winner = str(board[6]) + str(board[7]) + str(board[8])
        elif a == 3:
            winner = str(board[0]) + str(board[3]) + str(board[6])
        elif a == 4:
            winner = str(board[1]) + str(board[4]) + str(board[7])
        elif a == 5:
            winner = str(board[2]) + str(board[5]) + str(board[8])
        elif a == 6:
            winner = str(board[0]) + str(board[4]) + str(board[8])
        elif a == 7:
            winner = str(board[2]) + str(board[4]) + str(board[6])

        if winner == "XXX":
            return 'X'
        elif winner == "OOO":
            return 'O'

    for a in range(9):
        if a in board:
            break
        elif a == 8:
            return "draw"

    return None


def main():
    players = player_input()
    board = deque([''] * 9)
    board = populateEmptyBoard(board)
    display_board(board)
    startGame(board, players[0])


if __name__ == "__main__":
    main()