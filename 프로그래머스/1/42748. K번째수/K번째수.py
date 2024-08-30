def solution(array, commands):
    answer = []
    #commands순회하면서 2차원배열 commands안에 있는 각 행의 열 값을 0번째 부터 2번째         인덱스까지 i j k로 설정한다
    for i,j,k in commands:
        #각 행 마다 새로운 i j k에 따른 값을 새로 받기 위해 temp_arr 생성
        temp_arr = []
        #array배열을 i-1번째 부터 j-1번째까지 슬라이싱 한 값을 sorted함수를 사용하여             오름차순 정렬 -> i-1번째부터 하는 이유는 문제에서 인덱스기준으로 하는것이               아니기 때문
        temp_arr = sorted(array[i-1:j])
        #temp_arr의 k-1번째 인덱스 값을 answer에 append를 사용하여 적용
        answer.append(temp_arr[k-1])
    return answer
