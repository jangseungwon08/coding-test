from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons, len(dungeons)):
        temp = k
        count = 0
        for min_need, produce_need in i:
            if temp >= min_need:
                temp -= produce_need
                count +=1
        answer = max(count, answer)
    return answer