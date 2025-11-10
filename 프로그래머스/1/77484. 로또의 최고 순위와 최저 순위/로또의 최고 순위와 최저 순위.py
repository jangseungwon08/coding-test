def solution(lottos, win_nums):
    answer = []
    win_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    zero_count = 0
    hit_count = 0
    for i in lottos:
        if i == 0:
            zero_count += 1
        if i in win_nums:
            hit_count += 1
    max_hit = zero_count + hit_count
    min_hit = hit_count
    answer.append(win_dict[max_hit])
    answer.append(win_dict[min_hit])
    return answer