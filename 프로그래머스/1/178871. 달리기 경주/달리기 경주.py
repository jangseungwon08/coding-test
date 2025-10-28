def solution(players, callings):
    answer = []
    player_dict = dict()
#     k, i 를 뽑아서 딕셔너리로 만듬
    for v, i in enumerate(players):
        player_dict[i] = v
    for i in callings:
#         선수가 몇번째 순위에 있는지
        idx = player_dict[i]
#     호명된 player 순위 1 증가
        player_dict[i] -= 1
#     호명된 player 바로 앞 player의 순위 1감소 (players[idx-1] => 호명된 플레이어 바로 앞 player)
        player_dict[players[idx-1]] += 1
#     players에도 player_dict과 같이 업데이트 해줌
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players