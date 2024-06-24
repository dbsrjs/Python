dic={"코카콜라":1400, "사이다":1300, "밀키스":1100, "커피":1250, "삼다수":700,"몬스터":2300} 
a_list = []
b_list = []

def 거스름돈(num):
    list=[]
    if(num > 0):
        for a in range(0,len(str(num))):
            list.append(int(str(num)[a]))
        print("\n거스름돈으로 50000원", list[0],"개", "10000원", list[1], "개, ", "5000원", list[2],"개, ", "1000원", list[3],"개, ", "500원", list[4],"개, ", "100원", list[5],"개, ", "50원", list[6],"개, ", "10원", list[7],"개를 드리겠습니다.")
        print("총 %d원입니다."% (num))
    elif (num==0):
        print("\n거스름돈이 없습니다.")
    else:
        print("\n잘못된 금액을 넣으셨습니다.")
def price():    #가격
    plus = 0
    for f in range(0,len(a_list)):
        x=a_list[f]
        plus = plus+(dic[x]*b_list[f])
    return plus

print("안녕하세요 장쪽이 자판기입니다.")

print("\n저희 자판기의 음료 종류는", dic, "이 있습니다.")

while (True) :
    print("\n구매하실 음료명을 입력해주세요.")
    a = input("음료수 종류 : ")
    print()
    if (a in dic):
        print("구매하실 음료수의 개수를 입력해주세요.")  
        b = int(input("음료수 개수 : "))
        if(b>=0):
            c = input("\n음료수 더 고르실건가요?\n 1.네   2.아니요   : ")

            a_list.append(a)
            b_list.append(b)

            if (c == "네"):
                continue

            elif (c == "아니요"):
                g = price()
                while(True):
                    print("\n지불해야 할 가격은",g,"원입니다.")
                    num = int(input("돈을 넣어주세요. : "))
                    if num >= g:
                        for j in range(0,len(b_list)):
                            print("\n음료수",a_list[j]+"를",b_list[j],"개 만큼 드리겠습니다." )
                        거스름돈(num-g)
                        print("\n저희 장쪽이 자판기를 이용해주셔서 감사합니다.\n 안녕히가세요. :D")
                        exit()
                    elif num<g:
                        print()
                        print("\n잔액이 부족합니다.\n 잔액을 더 넣어주세요.")
                        g-=num
                        continue
        else:
            print("\n잘못된 개수를 넣었습니다.")

    elif (a=="비트코인"):
        print("  ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣶⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡿⠿⠛⠛⠛⠛⠛⠛⠻⢿⣿⣿⣦⣄⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⢠⣼⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣷⣄⠀⠀⠀ ")
        print("⠀⠀⠀⣰⣿⡿⠋⠀⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⢿⣿⣦⡀⠀⠀")
        print("⠀⠀⣸⣿⡿⠀⠀⠀⠸⠿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣶⣄⠀⠀⠀⠀⢹⣿⣷⠀")
        print("⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠈⣿⣿⣿⠀⠀⠀⠀⠀⢹⣿⣧⠀")
        print("⠀⣾⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⢀⣠⣿⣿⠟⠀⠀⠀⠀⠀⠈⣿⣿⠀")
        print("⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠿⠿⠿⣿⣿⣥⣄⠀⠀⠀⠀⠀⠀⣿⣿⠀")
        print("⠀⢿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⣧⠀⠀⠀⠀⢀⣿⣿⠀")
        print("⠀⠘⣿⣷⡀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⣼⣿⣿⡿⠀⠀⠀⠀⣸⣿⡟⠀")
        print("⠀⠀⢹⣿⣷⡀⠀⠀⢰⣶⣿⣿⣿⣷⣶⣶⣾⣿⣿⠿⠛⠁⠀⠀⠀⣸⣿⡿⠀")
        print("⠀⠀⠀⠹⣿⣷⣄⠀⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀⠀⢀⣾⣿⠟⠁⠀⠀")
        print("⠀⠀⠀⠀⠘⢻⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⡿⠋⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣴⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("\n2023년 5월 16일을 기준으로 1BTC당 36,720,133.39KRW 입니다.")

    else:
        print("\n존재하지 않는 제품입니다.\n제품명을 다시 입력해주세요.")
        continue
