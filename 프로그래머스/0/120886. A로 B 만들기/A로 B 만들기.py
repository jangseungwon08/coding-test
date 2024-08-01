def solution(before, after):
    '''
    answer = 0
    temp_before = 0
    temp_after = 0
    #after와 before길이 같으니까 인덱스 형식으로 순회
    for i in range(len(before)):
        #temp_before에 before의 아스키 코드 값 누적
        temp_before += ord(before[i])
        #temp_after에 after의 아스키 코드 값 누적
        temp_after += ord(after[i])
        #누적한 값이 같으면 1 다르면 0
    if temp_before == temp_after:
        answer = 1
    else:
        answer = 0
    return 0
        '''
    before = sorted(before)
    after = sorted(after)
    if before == after:
        return 1
    else: 
        return 0