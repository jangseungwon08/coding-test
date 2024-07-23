def solution(arr, intervals):
    answer = []
    #intervals를 for문을 돌리면 [1,3] -> [0,4]순으로 나온다. 2차원 배열이기 때문에
    for i in intervals:
        #intervals는 항상 a1 b1 a2 b2꼴로 주어진다고 했으니 [1,3]에서 각 원소 ai bi를 대입
        ai , bi = i
        #arr[ai:bi+1]까지 슬라이싱 bi+1의 이유는 슬라이싱은 -1까지 접근하기 때문
        answer += arr[ai:bi+1]
    return answer