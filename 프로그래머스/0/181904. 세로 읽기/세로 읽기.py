def solution(my_string, m, c):
    '''
    answer = ''
    #일단 my_string문자열을 각 원소로 나누어줘야되니까
    temp = []
    #my_string for문 돌리면서
    for i in my_string:
        #temp배열에 하나씩 다 넣어준다
        temp.append(i)
        #temp배열 슬라이싱으로 c-1번째부터 m칸 만큼 step밟아주면
    temp = temp[c-1::m]
    answer = ''.join(temp)
    '''
    answer = my_string[c-1::m]
    return answer
