def solution(answers):
    answer = []
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num_count = [0, 0, 0]
    for i in range(len(answers)):
        cir_index1 = i % len(num_1)
        cir_index2 = i % len(num_2)
        cir_index3 = i % len(num_3)
        if answers[i] == num_1[cir_index1]:
            num_count[0] += 1
        if answers[i] == num_2[cir_index2]:
            num_count[1] += 1
        if answers[i] == num_3[cir_index3]:
            num_count[2] += 1
    for i,v in enumerate(num_count):
        if v == max(num_count):
            answer.append(i+1)
    return answer