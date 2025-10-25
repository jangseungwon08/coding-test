def solution(babbling):
    answer = 0
    babbling_list = ["aya","ye","woo","ma"]
    for i in babbling:
        temp_word = i
        for k in babbling_list:
            if k * 2 in temp_word:
                break
            temp_word = temp_word.replace(k, " ")
        temp_word = temp_word.replace(" ", "")
        if len(temp_word) == 0:
            answer += 1
    return answer