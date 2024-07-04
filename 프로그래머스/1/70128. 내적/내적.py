def solution(a, b):
    answer = 0
    #a의 길이와 b의 길이가 같으니까 a의 길이를 구한 후 a의 각 원소값과 b의 각 원소값을 곱해서
    #다 더해주면 내적 길이가 나온다.
    #sum과 zip을 이용해서도 구할 수 있다.
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer