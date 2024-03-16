import random,sys

#색
red = '\033[31m \033[41m' + '■' + '\033[0m'
blue = '\033[34m \033[44m' + '■' + '\033[0m'
yellow = '\033[33m \033[43m' + '■' + '\033[0m'
green = '\033[32m \033[42m' + '■' + '\033[0m'
pink = '\033[35m \033[45m' + '■' + '\033[0m'
null = '\033[30m \033[40m' + '■' + '\033[0m'

a_list, b_list, c_list, d_list, e_list, f_list, g_list = [], [], [], [], [], [], [] #병

color_list = [red, blue, yellow, green, pink] #색을 모아둔 리스트

bottle_list = [a_list, b_list, c_list, d_list, e_list, f_list, g_list] #병을 모아둔 리스트

# 병에 모래를 랜덤으로 추가
for i in color_list:
    for j in range(4):
        bottle_list[random.randrange(len(bottle_list))].append(i) #bottle_list 중 랜덤으로 정해진 곳에 i 값 넣기

# 병 정리
if len(bottle_list[len(bottle_list)-1]) > 4:  # 가장 마지막 리스트의 길이가 4개 이상인지 확인.

    #마지막 리스트의 맨 위 값을 pop() 함수로 제거하고, 첫 번째 리스트에 append() 함수로 추가.
    for j in range(len(bottle_list[len(bottle_list)-1])-4):
        bottle_list[0].append(bottle_list[len(bottle_list)-1].pop())

for i in range(len(bottle_list)):
    #bottle_list[i]가 4가 될 때 까지 옆 리스트에 마지막 원소 값을 보내줌
    if len(bottle_list[i]) > 4:
        for j in range(len(bottle_list[i])-4):
            bottle_list[i+1].append(bottle_list[i].pop()) #i에 있는 원소를 pop해서 i+1에 append

while True:
    f=0

    #공백 생성
    # 각 리스트에 '4 - 원소의 개수'를 해서 나온 개수만큼 null 값을 추가
    for i in bottle_list:
        for j in range(4-len(i)):
            i.append(null)

    # 병 출력
    for i in range(3, -1, -1):
        for j in range(len(bottle_list)):
            print(bottle_list[j][i],end=" ")
        print()

    #클리어
    for i in range(len(bottle_list)):
        if bottle_list[i].count(bottle_list[i][0])==4:    #각 병에서 같은 색깔이 4개가 될 때
            f+=1

    if f == 7:  #반복문 멈추기
        break

    # 공백 제거
    #각 리스트에 null 값이 있다면 null 값을 제거
    for i in range(len(bottle_list)):
        for j in range(len(bottle_list[i])):
            if null in bottle_list[i]:
                bottle_list[i].pop()

    # 이동
    X = int(input("어디에서?(포기하실려면 '77'을 입력해주세요)"))-1
    if X == 76:
        print("다음에 또 도전해보세요.")
        sys.exit()
    Y = int(input("어디로?"))-1

    if (X > len(bottle_list)-1 or Y > len(bottle_list)-1 or X < 0 or Y < 0 or len(bottle_list[X]) == 0): #X, Y의 값이 bottle_list 길이를 초과하거나, 음수거나, X의 원소가 없을 때
        print("다시 입력해주세요.")
        continue


    if len(bottle_list[Y]) == 4:   #이동 하려는 곳(Y)의 원소의 개수가 0일 때
        print("이동시동 할려는 병이 꽉 차있어서 이동 할 수 없습니다")

    elif len(bottle_list[Y]) == 0 or bottle_list[X][len(bottle_list[X])-1] == bottle_list[Y][len(bottle_list[Y])-1]:   #이동 하려는 곳(Y)의 원소의 개수가 없거나, 이동 시키는 곳(X)의 끝 모래의 색과 이동 하려는 곳(Y)의 끝 모래의 색이 같을 때
        bottle_list[Y].append(bottle_list[X].pop())

    else:
        print("움직일 수 없습니다")

    print("---------------------------------------------")

#while문 탈출 시
print()
print("게임을 클리어하셨군요. 축하드립니다!")
