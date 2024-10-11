import random

# じゃんけんの手を定義
hands = ["グー", "チョキ", "パー"]

# 勝敗判定関数 (3人の勝者を判定)
def judge(players):
    # playersは[player, computer1, computer2]の手のリスト
    unique_hands = set(players)
    
    # 全員同じ手なら引き分け
    if len(unique_hands) == 1:
        return -1  # 引き分けを示す
    
    # グー、チョキ、パー全て出た場合も引き分け
    if len(unique_hands) == 3:
        return -1  # 引き分けを示す

    # 勝敗のルール
    # グー (0) がチョキ (1) に勝つ, チョキ (1) がパー (2) に勝つ, パー (2) がグー (0) に勝つ
    # 出た手が2種類の場合、どちらが強いかで勝者を決める
    if players.count(0) > 0 and players.count(1) > 0 and players.count(2) == 0:
        return players.index(0)  # グーが勝ち
    elif players.count(1) > 0 and players.count(2) > 0 and players.count(0) == 0:
        return players.index(1)  # チョキが勝ち
    elif players.count(2) > 0 and players.count(0) > 0 and players.count(1) == 0:
        return players.index(2)  # パーが勝ち

# 勝者の名前を取得
def get_winner_name(index):
    if index == 0:
        return "プレイヤー"
    elif index == 1:
        return "コンピュータ1"
    elif index == 2:
        return "コンピュータ2"
    else:
        return "引き分け"

# 3回勝負
rounds = 3
scores = [0, 0, 0]  # プレイヤー, コンピュータ1, コンピュータ2の勝利数

# ゲームの開始
print("じゃんけんをしましょう！")
print("0: グー, 1: チョキ, 2: パー")

for round_num in range(1, rounds + 1):
    print(f"\n--- {round_num}回戦 ---")

    # プレイヤーの手を入力
    player_choice = int(input("あなたの手を選んでください（0, 1, 2）: "))

    # コンピュータ1とコンピュータ2の手をランダムに選択
    computer1_choice = random.randint(0, 2)
    computer2_choice = random.randint(0, 2)

    # 各プレイヤーの手を表示
    print(f"あなたの手: {hands[player_choice]}")
    print(f"コンピュータ1の手: {hands[computer1_choice]}")
    print(f"コンピュータ2の手: {hands[computer2_choice]}")

    # 勝者を判定
    result = judge([player_choice, computer1_choice, computer2_choice])

    # 勝敗を表示し、勝者のスコアを加算
    if result == -1:
        print("このラウンドは引き分けです。")
    else:
        winner_name = get_winner_name(result)
        print(f"このラウンドの勝者: {winner_name}")
        scores[result] += 1

# 最終結果を表示
print("\n=== 最終結果 ===")
print(f"プレイヤーの勝利数: {scores[0]}")
print(f"コンピュータ1の勝利数: {scores[1]}")
print(f"コンピュータ2の勝利数: {scores[2]}")

# 最終的な勝者を決定
if scores.count(max(scores)) > 1:
    print("最終結果は引き分けです。")
else:
    final_winner = get_winner_name(scores.index(max(scores)))
    print(f"最終的な勝者は {final_winner} です！")