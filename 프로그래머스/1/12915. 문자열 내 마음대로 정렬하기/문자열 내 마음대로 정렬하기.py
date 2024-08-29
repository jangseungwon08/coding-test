def solution(strings, n):
    #strings를 정렬하는데 lambda를 사용하여 x의 n번째원소만 가져온다. 만약에 sun bed car가           있으면 u e a 만 가져온다. n번째 문자가 동일할 경우 전체 문자열 기준으로 다시 정렬함
    strings.sort(key = lambda x: (x[n], x))
    #lambda x: (x[n, x])는 x[n]을 기준으로 먼저 오름차순 정렬하고 x에 대해서 정렬한다.
    #-> 정렬할 아이템이 중복될 경우에는 튜플로 순서를 내보내주면 된다.
    return strings