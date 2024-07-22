def solution(n_str):
    #lstrip함수(문자열에 왼쪽 공백이나 인자가된 문자열 모두 제거)
    #제거는 strip함수 사용하면 유용하다.
    answer = n_str.lstrip('0')
    return answer