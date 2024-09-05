def solution(sizes):
    answer = 0
    for i in sizes:
        if i[1] > i[0]:
            i[1], i[0] = i[0] , i[1]
    h_size = max([i[1] for i in sizes])
    w_size = max([i[0] for i in sizes])
    return h_size * w_size