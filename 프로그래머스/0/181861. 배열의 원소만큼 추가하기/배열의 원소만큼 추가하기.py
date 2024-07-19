def solution(arr):
    answer = []
    #arr을 for문을 돌려서 i를 이터러블한 객체로 만들어준 뒤 i를 곱하면 [i]가 i만큼 반복되어서 나온다. 그 값을 answer에 저장하면서 for문을 돌리면 됨
    for i in arr:
        answer += [i]*i      
    return answer