def solution(k, score):
    answer = []
    honest_k = []
    for i in range(len(score)):
        if k > len(honest_k):
            honest_k.append(score[i])
            honest_k.sort(reverse=True)
            answer.append(honest_k[-1])
        else:
            if score[i] > honest_k[-1]:
                honest_k.remove(honest_k[-1])
                honest_k.append(score[i])
                honest_k.sort(reverse=True)
                answer.append(honest_k[-1])
            else:
                answer.append(honest_k[-1])
    return answer