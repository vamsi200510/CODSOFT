import math
print("TIC TAC TOE GAME LOADED")
print("PROGRAM STARTED")
input("Press Enter to continue...")

board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    win_combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def minimax(is_max):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if ' ' not in board:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

def main():
    print("TIC TAC TOE (You = X, AI = O)")
    print("Positions:")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8")

    while True:
        print_board()

        move = int(input("Enter position (0-8): "))
        if board[move] != ' ':
            print("Position already taken!")
            continue

        board[move] = 'X'

        if check_winner('X'):
            print_board()
            print("🎉 You win!")
            break

        if ' ' not in board:
            print("😐 It's a draw!")
            break

        ai_move()

        if check_winner('O'):
            print_board()
            print("🤖 AI wins!")
            break

if __name__ == "__main__":
    main()
