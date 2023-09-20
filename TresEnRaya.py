import random

# Función para imprimir el tablero
def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i * 3 + j] if board[i * 3 + j] != ' ' else ' ', end=' | ')
        print()
        if i < 2:
            print("-----------")

# Función para verificar si alguien ha ganado
def check_win(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Función para obtener las celdas vacías en el tablero
def get_empty_cells(board):
    return [i for i in range(len(board)) if board[i] == ' ']

# Función para que la máquina tome una decisión utilizando el algoritmo Minimax con poda alfa-beta
def tttplayer(board, cross):
    if cross:
        player = 'X'
        opponent = 'O'
    else:
        player = 'O'
        opponent = 'X'

    # Función Minimax con poda alfa-beta
    def minimax(board, depth, is_maximizing, alpha, beta):
        if check_win(board, opponent):
            return -1
        if check_win(board, player):
            return 1
        if len(get_empty_cells(board)) == 0:
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for move in get_empty_cells(board):
                board[move] = player
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[move] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in get_empty_cells(board):
                board[move] = opponent
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[move] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    if len(get_empty_cells(board)) == 9:
        # Si es el primer movimiento, elige una esquina al azar
        move = random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
    else:
        best_move = None
        best_eval = float('-inf') if cross else float('inf')
        for move in get_empty_cells(board):
            board[move] = player
            eval = minimax(board, 0, False, float('-inf'), float('inf'))
            board[move] = ' '
            if cross:
                if eval > best_eval:
                    best_eval = eval
                    best_move = move
            else:
                if eval < best_eval:
                    best_eval = eval
                    best_move = move
        move = (best_move // 3, best_move % 3)

    return move

# Función principal del juego
def main():
    while True:
        print("Bienvenido al juego de tres en raya.")
        choice = input("Por favor, elija X o O (X siempre comienza): ").upper()

        if choice not in ('X', 'O'):
            print("Por favor, elija X o O.")
            continue

        cross = True if choice == 'X' else False
        board = [' '] * 9

        print_board(board)

        #Si el jugador es Cruz:

        if cross:
            while True:
                if cross:
                    print("Turno de X")
                    x, y = map(int, input("Introduzca la tupla de su movimiento (fila, columna): ").split(','))
                    move = x * 3 + y
                else:
                    print("Turno de O (Máquina)")
                    x, y = tttplayer(board, cross)
                    move = x * 3 + y

                if board[move] != ' ':
                    print("Esa casilla ya está ocupada. Por favor, elija otra.")
                    continue

                board[move] = 'X' if cross else 'O'
                print_board(board)

                if check_win(board, 'X' if cross else 'O'):
                    if cross:
                        print("¡Felicidades! ¡Has ganado!")
                    else:
                        print("Mala suerte, te gané.")
                    break

                if ' ' not in board:
                    print("¡Empate!")
                    break

                cross = not cross

            play_again = input("¿Quieres jugar de nuevo? (S/N): ").upper()
            if play_again != 'S':
                break

        #Si el jugador no es Cruz:
        else:
            while True:
                if cross == False:
                    print("Turno de X (Máquina)")
                    x, y = tttplayer(board, cross)
                    move = x * 3 + y
                else:
                    print("Turno de O")
                    x, y = map(int, input("Introduzca la tupla de su movimiento (fila, columna): ").split(','))
                    move = x * 3 + y

                if board[move] != ' ':
                    print("Esa casilla ya está ocupada. Por favor, elija otra.")
                    continue

                board[move] = 'O' if cross else 'X'
                print_board(board)

                if check_win(board, 'O' if cross else 'X'):
                    if cross:
                        print("¡Felicidades! ¡Has ganado!")
                    else:
                        print("Mala suerte, te gané.")
                    break

                if ' ' not in board:
                    print("¡Empate!")
                    break

                cross = not cross

            play_again = input("¿Quieres jugar de nuevo? (S/N): ").upper()
            if play_again != 'S':
                break

if __name__ == "__main__":
    main()
