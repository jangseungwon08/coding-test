def solution(num_list, n):
    #num_list//n의 길이만큼 범위 순회 한 값에 num_list[n*i:n*(i+1)]의 길이까지 슬라이싱
    #ex) n = 2이고 i가 0 1 2 3 이면 num_list[0:1] num_list[2:3] num_list[4:5]이런식으로 
    #두개의 원소값을 접근하면서 순회가능
    answer = [num_list[n*i:n*(i+1)] for i in range(len(num_list)//n)]
    return answer