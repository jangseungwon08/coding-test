import math
def solution(n, words):
#     1. 이전단어 마지막 글자와 이번단어 첫 글자가 다를 때 탈락
#     2. 같은 단어가 나오면 탈락
    for i in range(1,len(words)):
        if (words[i][0] != words[i-1][-1]) or (words[i] in words[:i]):
            return [i%n +1, i //n + 1]
    return [0,0]