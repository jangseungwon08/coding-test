def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    for i in range(len(num_list)):
        #i %2 가 값이 존재한다. -> 인덱스에서 홀수이다. 하지만 가장 첫번째 원소를 1번 원소라고했           으니까 even(짝수)에 대입시켜야된다.
        if i % 2:
            even += num_list[i]
            #반대로 생각하면 된다.
        else:
            odd += num_list[i]
    if odd > even:
        answer = odd
    else:
        answer = even
    return answer