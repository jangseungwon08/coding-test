def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        temp_list = []
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
            elif prices[i] <= prices[j]:
                temp_list.append(1)
        if sum(temp_list) == len(prices) - (i+1):
            answer.append(sum(temp_list))
    answer.append(0)
    return answer