def solution(n):
    answer = ''
    #n이 3이면 '수박수박수박'
    a = '수박'*n
    #a '수박수박수박이' a[2]까지 따라서 '수박수' return
    answer = a[:n]
    return answer
