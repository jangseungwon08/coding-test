def solution(numlist, n):
    answer = []
    #sorted함수를 사용하여 numlist를 정렬하는데 key값이 abs(n-x)의 값 즉 n-x의 절대값      을 기준오름차순 정렬을 하는데 abs(n-x)의 값이 같으면 n-x가 큰 값을 기준으로 정렬
    temp = sorted(numlist, key = lambda x:( abs(n-x), n-x))
    return temp