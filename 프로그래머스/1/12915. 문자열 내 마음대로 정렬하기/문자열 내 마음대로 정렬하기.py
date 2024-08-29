def solution(strings, n):
    #strings를 정렬하는데 lambda를 사용하여 x의 n번째원소만 가져온다. 만약에 sun bed car가           있으면 u e a 만 가져온다. n번째 문자가 동일할 경우 전체 문자열 기준으로 다시 정렬함
    strings.sort(key = lambda x: (x[n], x))
    return strings