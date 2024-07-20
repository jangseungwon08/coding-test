def solution(arr):
    answer = ''
    #join 함수를 사용하여 ''를 기준으로 문자열을 이어붙인다. "a", "b"가 이렇게 있으니
    #''를 기준으로 붙이면 ab가된다.
    answer = ''.join(arr)
    return answer