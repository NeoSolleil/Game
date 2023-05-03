'''

import random

def get_card():
    """ランダムなカードを取得する"""
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(deck)

def calculate_score(hand):
    """手札の得点を計算する"""
    score = 0
    num_aces = 0
    for card in hand:
        if card == 'A':
            num_aces += 1
            score += 11
        elif card in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(card)
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    return score

def play():
    """ゲームをプレイする"""
    player_hand = [get_card(), get_card()]
    dealer_hand = [get_card(), get_card()]
    print(f"ディーラーの手札: [{dealer_hand[0]}, *]")
    print(f"あなたの手札: {player_hand} (得点: {calculate_score(player_hand)})")
    while True:
        action = input("カードを引きますか？(y/n): ")
        if action.lower() == 'y':
            player_hand.append(get_card())
            score = calculate_score(player_hand)
            print(f"あなたの手札: {player_hand} (得点: {score})")
            if score > 21:
                print("バスト！あなたの負けです。")
                return
        else:
            print(f"ディーラーの手札: {dealer_hand} (得点: {calculate_score(dealer_hand)})")
            while calculate_score(dealer_hand) < 17:
                dealer_hand.append(get_card())
                print(f"ディーラーがカードを引きました: {dealer_hand[-1]}")
            dealer_score = calculate_score(dealer_hand)
            if dealer_score > 21:
                print("ディーラーがバストしました！あなたの勝ちです。")
            if dealer_score > score:
                print("ディーラーの勝ちです。")
            if dealer_score < score:
                print("あなたの勝ちです！")
            if dealer_score == score:
                print("引き分けです！")
            return

if __name__ == '__main__':
    play()
'''

import random

def get_card():
    """ランダムなカードを取得する"""
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(deck)



def calculate_score(hand):
    """手札の得点を計算する"""
    global score
    score =0
    num_aces = 0
    for card in hand:
        if card == 'A':
            num_aces += 1
            score += 11
        elif card in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(card)
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    return score

def play():
    """ゲームをプレイする"""
    player_hand = [get_card(), get_card()]
    dealer_hand = [get_card(), get_card()]
    print(f"ディーラーの手札: [{dealer_hand[0]}, *]")
    print(f"あなたの手札: {player_hand} (得点: {calculate_score(player_hand)})")
    while True:
        action = input("カードを引きますか？(y/n): ")
        if action.lower() == 'y':
            player_hand.append(get_card())
            score = calculate_score(player_hand)
            print(f"あなたの手札: {player_hand} (得点: {score})")

            if score > 21:
                print("バスト！あなたの負けです。")
                return
        else:
            score = calculate_score(player_hand)
            print(f"ディーラーの手札: {dealer_hand} (得点: {calculate_score(dealer_hand)})")
            while calculate_score(dealer_hand) < 17:
                dealer_hand.append(get_card())
                print(f"ディーラーがカードを引きました: {dealer_hand[-1]}")
            dealer_score = calculate_score(dealer_hand)
            if dealer_score > 21:
                print("ディーラーがバストしました！あなたの勝ちです。")
            elif dealer_score > score:
                print("ディーラーの勝ちです。")
            elif dealer_score < score:
                print("あなたの勝ちです！")
            else:
                print("引き分けです！")
            return

if __name__ == '__main__':
    play()
