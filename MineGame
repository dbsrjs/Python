import random
import sys

sys.setrecursionlimit(2**30)  # 재귀 호출의 깊이 제한을 늘림

null = "\033[30m\033[100m" + "X" + "\033[0m"  # 빈 칸을 나타내는 변수
red = "\033[31m\033[41m" + "p" + "\033[0m"  # 깃발을 나타내는 변수

mode = "오리지널"


def Mine(x, y, boom):   # 지뢰찾기 게임판을 생성하는 함수
    global boom_location
    global panel
    global row
    global line

    row = x  # 판의 가로 크기 설정
    line = y  # 판의 세로 크기 설정

    panel = [[null for i in range(x)] for i in range(y)]  # 보일 화면을 생성
    boom_location = [["?" for i in range(x)]
                     for i in range(y)]  # 폭탄이 있을 공간을 생성

    for i in range(boom):  # 랜덤으로 지뢰를 개수에 맞게 넣기
        Random_boom(x, y)
        while boom_location[boom_y][boom_x] != "?":
            Random_boom(x, y)
        boom_location[boom_y][boom_x] = "B"
    
    for j in range(line):
        for i in range(row):
            boom_number = 0
            
            # 주변 8칸에 대해 폭탄이 있는지 확인하고, 폭탄이 있으면 boom_number를 1 증가시킴
            if boom_location[j][i] == "?":
                if 0 <= i - 1 and row - 1 >= i - 1 and 0 <= j - 1 and line - 1 >= j - 1:
                    if boom_location[j - 1][i - 1] == "B":
                        boom_number += 1

                if 0 <= i and row - 1 >= i and 0 <= j - 1 and line - 1 >= j - 1:
                    if boom_location[j - 1][i] == "B":
                        boom_number += 1

                if 0 <= i + 1 and row - 1 >= i + 1 and 0 <= j - 1 and line - 1 >= j - 1:
                    if boom_location[j - 1][i + 1] == "B":
                        boom_number += 1

                if 0 <= i - 1 and row - 1 >= i - 1 and 0 <= j and line - 1 >= j:
                    if boom_location[j][i - 1] == "B":
                        boom_number += 1

                if 0 <= i + 1 and row - 1 >= i + 1 and 0 <= j and line - 1 >= j:
                    if boom_location[j][i + 1] == "B":
                        boom_number += 1

                if 0 <= i - 1 and row - 1 >= i - 1 and 0 <= j + 1 and line - 1 >= j + 1:
                    if boom_location[j + 1][i - 1] == "B":
                        boom_number += 1

                if 0 <= i and row - 1 >= i and 0 <= j + 1 and line - 1 >= j + 1:
                    if boom_location[j + 1][i] == "B":
                        boom_number += 1

                if 0 <= i + 1 and row - 1 >= i + 1 and 0 <= j + 1 and line - 1 >= j + 1:
                    if boom_location[j + 1][i + 1] == "B":
                        boom_number += 1

                boom_location[j][i] = str(boom_number)


def Random_boom(x, y):  # 지뢰의 위치를 랜덤하게 결정하는 함수
    global boom_x
    global boom_y

    boom_x = random.randint(0, x - 1)  # 지뢰의 x좌표를 랜덤하게 결정
    boom_y = random.randint(0, y - 1)  # 지뢰의 y좌표를 랜덤하게 결정


def Open(x, y): # 칸을 여는 함수
    if boom_location[User_y - 1][User_x - 1] == "B":  # 고른 곳에 폭탄이 있을 경우
        panel[User_y - 1][User_x - 1] = "B"
        View()
        print("지뢰 해체 실패")
        sys.exit()

    if panel[y - 1][x - 1] != red:  #선택한 좌표가 깃발이 아니라면 열어주기(숫자로 표시)
        panel[y - 1][x - 1] = boom_location[y - 1][x - 1]

    if boom_location[y - 1][x - 1] == "0" and panel[y - 1][x - 1] != red:
        if 0 <= y - 2 and line - 1 >= y - 2 and 0 <= x - 2 and x - 2 <= row - 1:
            if boom_location[y - 2][x - 2] == "0" and panel[y - 2][x - 2] == null:
                Open(x - 1, y - 1)

        if 0 <= y - 2 and line - 1 >= y - 2 and 0 <= x - 1 and row - 1 >= x - 1:
            if boom_location[y - 2][x - 1] == "0" and panel[y - 2][x - 1] == null:
                Open(x, y - 1)

        if 0 <= y - 2 and line - 1 >= y - 2 and 0 <= x and row - 1 >= x:
            if boom_location[y - 2][x] == "0" and panel[y - 2][x] == null:
                Open(x + 1, y - 1)

        if 0 <= y - 1 and line - 1 >= y - 1 and 0 <= x - 2 and row - 1 >= x - 2:
            if boom_location[y - 1][x - 2] == "0" and panel[y - 1][x - 2] == null:
                Open(x - 1, y)

        if 0 <= y - 1 and line - 1 >= y - 1 and 0 <= x and row - 1 >= x:
            if boom_location[y - 1][x] == "0" and panel[y - 1][x] == null:
                Open(x + 1, y)

        if 0 <= y and line - 1 >= y and 0 <= x - 2 and row - 1 >= x - 2:
            if boom_location[y][x - 2] == "0" and panel[y][x - 2] == null:
                Open(x - 1, y + 1)

        if 0 <= y and line - 1 >= y and 0 <= x - 1 and row - 1 >= x - 1:
            if boom_location[y][x - 1] == "0" and panel[y][x - 1] == null:
                Open(x, y + 1)

        if 0 <= y and line - 1 >= y and 0 <= x and row - 1 >= x:
            if boom_location[y][x] == "0" and panel[y][x] == null:
                Open(x + 1, y + 1)

    if boom_location[y - 1][x - 1] == "0" and panel[y - 1][x - 1] != red:
        if 0 <= y - 2 and line - 1 >= y - 2 and 0 <= x - 2 and x - 2 <= row - 1 and panel[y - 2][x - 2] != red:
            panel[y - 2][x - 2] = boom_location[y - 2][x - 2]

        if 0 <= y - 2 and line - 1 >= y - 2 and 0 <= x - 1 and row - 1 >= x - 1 and panel[y - 2][x - 1] != red:
            panel[y - 2][x - 1] = boom_location[y - 2][x - 1]

        if 0 <= y - 2 and line - 1 >= y - 2 and 0 <= x and row - 1 >= x and panel[y - 2][x] != red:
            panel[y - 2][x] = boom_location[y - 2][x]

        if 0 <= y - 1 and line - 1 >= y - 1 and 0 <= x - 2 and row - 1 >= x - 2 and panel[y - 1][x - 2] != red:
            panel[y - 1][x - 2] = boom_location[y - 1][x - 2]

        if 0 <= y - 1 and line - 1 >= y - 1 and 0 <= x and row - 1 >= x and panel[y - 1][x] != red:
            panel[y - 1][x] = boom_location[y - 1][x]

        if 0 <= y - 1 and line - 1 >= y and 0 <= x - 2 and row - 1 >= x - 2 and panel[y][x - 2] != red:
            panel[y][x - 2] = boom_location[y][x - 2]

        if 0 <= y and line - 1 >= y and 0 <= x - 1 and row - 1 >= x - 1 and panel[y][x - 1] != red:
            panel[y][x - 1] = boom_location[y][x - 1]

        if 0 <= y and line - 1 >= y and 0 <= x and row - 1 >= x and panel[y][x] != red:
            panel[y][x] = boom_location[y][x]


def View(): # 게임 판을 출력하는 함수
    for i in range(line):   #Y
        for j in range(row):    #X
            print(panel[i][j], end=" ")  # 각 칸을 공백으로 구분해 출력
        print()  # 각 행을 개행으로 구분


def 깃발(x, y): # 깃발을 세우는 함수
    if panel[y - 1][x - 1] == null:  # 선택한 칸이 비어있다면 깃발 지정
        panel[y - 1][x - 1] = red  
    elif panel[y - 1][x - 1] == red:  # 선택한 칸에 깃발이 있다면 깃발 제거
        panel[y - 1][x - 1] = null  


def Win():  # 승리

    a = 0

    for i in range(row):
        for j in range(line):
            if boom_location[i][j] != "B":
                if (panel[i][j] == boom_location[i][j]):
                    a = 1

                else:
                    a = 0
                    return 0

    if a == 1:
        View()
        print("승리")
        sys.exit()


while True: # 난이도를 입력받아 게임을 시작하는 코드

    try:
        difficulty = input("난이도를 입력해 주세요(초급, 중급, 고급, 최고급, 사용자 지정) : ").strip()

        if difficulty == "초급":
            Mine(9, 9, 10)

        elif difficulty == "중급":
            Mine(16, 16, 40)

        elif difficulty == "고급":
            Mine(30, 16, 99)

        elif difficulty == "최고급":
            Mine(10, 24, 160)

        elif difficulty == "사용자 지정" or difficulty == "사용자지정":
            x = int(input("x값을 입력해주세요 : "))
            y = int(input("y값을 입력해주세요 : "))
            boom = int(input("지뢰의 개수를 입력해주세요 : "))
            Mine(x, y, boom)

            if x * y <= boom:
                print("폭탄이 더 많음")
                continue

        else:
            print("다시 입력해주십시오.")
            continue

        break

    except:
        print("다시")


print('"P"를 입력하면 깃발(지뢰) 모드로, "O"(오리지널)를 입력하면 일반 모드로 전환됩니다.')
# 게임 모드에 따라 깃발을 세우거나 칸을 열거나 하는 코드
while True:
    View()
    try:
        mode_유무 = input("(x, y)").strip()

    except:
        print("다시")
        continue

    if mode_유무 == "P" or mode_유무 == "p":
        mode = "깃발"
        print("지뢰 모드")

    elif mode_유무 == "O" or mode_유무 == "o":
        mode = "오리지널"
        print("오리지널 모드")

    else:
        try:
            User_x, User_y = map(int, mode_유무.split(","))
            if User_x <= 0 or User_y <= 0 or User_x > row or User_y > line:
                print("좌표를 다시 입력해주세요")
                continue

            if mode == "깃발":
                깃발(User_x, User_y)

            if mode == "오리지널":
                Open(User_x, User_y)
        except ValueError:
            print("다시 입력")

    Win()  # 승리 조건 확인
