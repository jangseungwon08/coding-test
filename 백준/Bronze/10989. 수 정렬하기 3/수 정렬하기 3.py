import sys
input = sys.stdin.readline
n = int(input())
#입력값이 10001까지 나오니까 10001번째 수 까지 0인 10001개 리스트 생성
n_list = [0]*10001
#n범위 만큼 순회하면서 n_list의 input()의 정수번째 인덱스 값 1 증가
#ex) int(input())의 인덱스 값이 1 2 3 3이면 n_list = [0, 1, 1, 2]가 됨
for _ in range(n):
    n_list[int(input())] += 1
#n_list길이 만큼 순회하면서(10000)까지 
for i in range(len(n_list)):
    #n_list[i]번째가 0이 아니면
    if n_list[i] != 0:
        #n_list의 i번째 원소 범위 만큼 ex) n_list= [ 0, 1, 1, 2]이면
        #n_list[3]의 값이면 0 1 까지 i 출력 --> 2번 출력
        for _ in range(n_list[i]):
            print(i)
