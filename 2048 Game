import random

# 2048 게임 보드 초기화
board = [[0] * 4 for _ in range(4)]

# 빈 셀 중 하나에 랜덤하게 숫자 2 또는 4 배치
def place_random_tile():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

# 게임 보드 출력
def print_board():
    for row in board:
        print(' '.join(str(cell) for cell in row))

# 이동 방향에 따라 타일을 이동시키고 합치는 로직
def move_tiles(direction):
    if direction == 'w':  # 위로 이동
        for j in range(4):
            for i in range(1, 4):
                if board[i][j] != 0:
                    x = i
                    while x > 0 and board[x-1][j] == 0:
                        board[x-1][j] = board[x][j]
                        board[x][j] = 0
                        x -= 1
                    if x > 0 and board[x-1][j] == board[x][j]:
                        board[x-1][j] *= 2
                        board[x][j] = 0

    elif direction == 's':  # 아래로 이동
        for j in range(4):
            for i in range(2, -1, -1):
                if board[i][j] != 0:
                    x = i
                    while x < 3 and board[x+1][j] == 0:
                        board[x+1][j] = board[x][j]
                        board[x][j] = 0
                        x += 1
                    if x < 3 and board[x+1][j] == board[x][j]:
                        board[x+1][j] *= 2
                        board[x][j] = 0

    elif direction == 'a':  # 왼쪽으로 이동
        for i in range(4):
            for j in range(1, 4):
                if board[i][j] != 0:
                    y = j
                    while y > 0 and board[i][y-1] == 0:
                        board[i][y-1] = board[i][y]
                        board[i][y] = 0
                        y -= 1
                    if y > 0 and board[i][y-1] == board[i][y]:
                        board[i][y-1] *= 2
                        board[i][y] = 0

    elif direction == 'd':  # 오른쪽으로 이동
        for i in range(4):
            for j in range(2, -1, -1):
                if board[i][j] != 0:
                    y = j
                    while y < 3 and board[i][y+1] == 0:
                        board[i][y+1], board[i][y] = board[i][y], board[i][y+1]
                        y += 1
                    if y < 3 and board[i][y+1] == board[i][y]:
                        board[i][y+1] *= 2
                        board[i][y] = 0


# 게임 상태 체크
def check_game_status():
    # 2048 타일이 있는 경우 승리
    for row in board:
        if 2048 in row:
            return 'win'

    # 빈 셀이 없는 경우
    if all(cell != 0 for row in board for cell in row):
        # 가로 방향으로 인접한 타일이 같은 경우
        for i in range(4):
            for j in range(3):
                if board[i][j] == board[i][j+1]:
                    return 'continue'

        # 세로 방향으로 인접한 타일이 같은 경우
        for j in range(4):
            for i in range(3):
                if board[i][j] == board[i+1][j]:
                    return 'continue'

        # 더 이상 이동할 수 없는 경우 패배
        return 'lose'

    return 'continue'

# 보드의 상태가 변했는지 확인하는 함수
def is_board_changed(old_board, new_board):
    return old_board != new_board

# 게임 시작
def start_game():
    place_random_tile()
    place_random_tile()
    print_board()

    while True:
        move = input("이동 방향을 입력하세요 (w: 위, s: 아래, a: 왼쪽, d: 오른쪽): ")

        if move in ['w', 's', 'a', 'd']:
            old_board = [row.copy() for row in board]
            move_tiles(move)
            if is_board_changed(old_board, board):
                place_random_tile()
            print_board()

            status = check_game_status()
            if status == 'win':
                print("승리하셨습니다!")
                break
            elif status == 'lose':
                print("패배하셨습니다.")
                break
        else:
            print("올바른 이동 방향을 입력하세요.")

# 게임 실행
start_game()
