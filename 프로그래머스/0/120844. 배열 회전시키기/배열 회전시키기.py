def solution(numbers, direction):
    answer = []
    if direction == 'right':
        #numbers[len(numbers)-1:]이면 numbers길이 -1만큼 부터 끝까지이다.                          즉 마지막 원소를 가져온다는 뜻이다.
        #numbers[:len(numbers)-1]ex)len(numbers)=3 이면 처음부터 2까지 마지막 인덱스는 
        #포함되지 않으니까 1번째 원소까지 포함시킨다. 따라서 1 2 
        answer = numbers[len(numbers)-1:] + numbers[:len(numbers)-1]
    elif direction == 'left':
        #1번째 원소부터 끝까지 1스텝씩
        #0번째 원소부터 1-1까지 즉 0번째 원소를 넣어준다.
        answer = numbers[1::1] + numbers[:1]
    return answer