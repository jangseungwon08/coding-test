def solution(i, j, k):
    answer = 0
    #i부터 j+1(j)까지의 범위까지 1칸씩 순회하면서
    for a in range(i , j+1):
        #str(a)의 문자열 안에서 str(k)가 나오는 횟수를 answer에 누적 저장
        answer += str(a).count(str(k))
    return answer