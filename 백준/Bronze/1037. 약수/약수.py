#n의 약수의 개수
n = int(input())
#n의 진짜 약수
n_list = list(map(int,input().split()))
#n의 개수가 1이면 n_list에 제곱을 한 값을 출력
if len(n_list) == 1:
    print(n_list[0]**2)
#양수 A가 N의 진짜 약수가 되려면 N이 A의 배수
#A가 1과 N이 아니어야 한다 라고 제한사항이 있다.
#따라서 가장 작은 원소값과 큰 원소값을 곱한값이 A의 값이 된다.
else:
    print(max(n_list)*min(n_list))