def solution(my_string, is_suffix):
    answer = 0
    '''
    temp = []
    #접두사인지 확인하기와 같은 문제
    for i in range(len(my_string)):
        temp.append(my_string[i:])
        if is_suffix in temp:
            answer = 1
        else:
            answer = 0
            '''
    #len(is_suffix)를 사용하여 길이만큼 뒤에서부터 끝까지 인덱싱을 한 값이 is_suffix와 값이 같      다.
    answer = int(my_string[-len(is_suffix):] == is_suffix)
    return answer