# リスト内の最大値をalice bobの順に取得する
def card_game(card_list: list[int]) -> int:
    alice, bob = 0, 0 
    while len(card_list) > 0:
        alice_score = max(card_list)
        alice += alice_score
        alice_score_index = card_list.index(alice_score)
        card_list.pop(alice_score_index)

        if len(card_list) == 0:
            break

        bob_score = max(card_list)
        bob += bob_score
        bob_score_index = card_list.index(bob_score)
        card_list.pop(bob_score_index)

    return alice - bob


if __name__ == "__main__":
    N = int(input())
    card_list = list(map(int, input().split()))
    print(card_game(card_list))