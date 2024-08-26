def solution(s, skip, index):
    answer = ''
    #알파벳 다 해줌
    temp_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in skip:
        if i in temp_alpha:
            temp_alpha.remove(i)
    for j in s:
        if temp_alpha.index(j) + index < len(temp_alpha):
            temp_index = temp_alpha.index(j) + index
            answer += temp_alpha[temp_index]
        else:
            temp_index = (temp_alpha.index(j) + index) % len(temp_alpha)
            answer += temp_alpha[temp_index]
    return answer