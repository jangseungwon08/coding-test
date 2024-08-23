def solution(my_string, overwrite_string, s):
    answer = ''
    #my_string처음의 s-1까지 슬라이싱 + overwrite_string 전체 + 남은 s+len(overwrite_string)길이 만큼 출력 하고 남은 부분 출력
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer