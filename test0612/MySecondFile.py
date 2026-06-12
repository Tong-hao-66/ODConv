import random
 
def rock_paper_scissors():
    choices = ['石头', '剪刀', '布']
    computer_choice = random.choice(choices)
    player_choice = input("请输入你的选择（石头、剪刀、布）: ")
 
    if player_choice not in choices:
        print("无效输入，请重新运行游戏。")
    else:
        if player_choice == computer_choice:
            print("平局！")
        elif (player_choice == '石头' and computer_choice == '剪刀') or \
             (player_choice == '剪刀' and computer_choice == '布') or \
             (player_choice == '布' and computer_choice == '石头'):
            print("你赢了！")
        else:
            print("你输了！")
        print(f"计算机的选择是: {computer_choice}")
 
if __name__ == "__main__":
    rock_paper_scissors()
