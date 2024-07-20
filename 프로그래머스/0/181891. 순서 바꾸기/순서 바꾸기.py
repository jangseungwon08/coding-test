def solution(num_list, n):
    answer = []
    #num_list[n:]은 num_list의 n번째 이후의 원소이다. 왜냐하면 인덱스로 접근하면 0 1 부터 
    #시작하기 때문에 n=1이고, num_list가 [2,1,6]이면 1부터 6까지 의 원소값을 answer에 대입한다.
    #num_list[:n]은 0부터 n-1번째 원소까지이다. 왜냐하면 n번째까지의 원소를 원하니까 n-1번째 
    #원소까지만 해주면 된다.
    answer = num_list[n:] + num_list[:n]
    return answer