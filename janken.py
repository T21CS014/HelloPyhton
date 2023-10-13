import random

# 選択肢
choices = [0, 1, 2]

# プレイヤーの選択を受け付ける関数
def get_player_choice():
    print("じゃんけんを始めます！")
    print("1: グー")
    print("2: チョキ")
    print("3: パー")
    choice = int(input("選んでください (1/2/3): "))
    return choices[choice - 1]

# コンピュータの選択をランダムに生成する関数
def get_computer_choice():
    return random.choice(choices)

# 勝敗を判定する関数
def determine_winner(player, computer):
    if player == computer:
        return "引き分け"
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        return "Aの勝ち"
    else:
        return "Bの勝ち"


# ゲームのメインループ

def p(a):
    if a==0:
        return "グー"
    if a==1:
        return "チョキ"
    if a==2:
        return "パー"

def main():
    #player_choice = get_player_choice()
    
        computer_choice = get_computer_choice()
        computer_choice_2 = get_computer_choice()

        result = determine_winner(computer_choice_2, computer_choice)
        print(f"Aの手: {p(computer_choice_2)} v.s Bの手: {p(computer_choice)} →　{result}")

        
