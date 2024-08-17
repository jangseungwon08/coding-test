def solution(array):
    answer = 0
    temp_dic = {}
    keys = []
    for i in array:
        temp_dic[i] = array.count(i)
    max_value = max(temp_dic.values())
    for k, v in temp_dic.items():
        if v == max_value:
            keys.append(k)
    if len(keys) > 1:
        return -1
    else:
        return keys[0]