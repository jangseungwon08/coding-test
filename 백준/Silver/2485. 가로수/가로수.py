#최대 공약수를 활용해서 푸는 문제
import sys
input = sys.stdin.readline
N = int(input())
N_list = [int(input())]
intervals = []
# 유클리드 호제법
def gcd(a,b):
    while b >0:
        a, b = b, a % b
    return a

for _ in range(1,N):
    N_list.append(int(input()))
    intervals.append(N_list[_] - N_list[_-1])
# 최대 공약수로 구하는 간격의 초기값을 입력해주고
max_num = intervals[0]

for i in range(1,len(intervals)):
# 최대 공약수를 이용해서 추가할 수 있는 나무를 최소화 한다.
# --> 나무의 간격을 최대화 해야된다
    max_num = gcd(max_num,intervals[i])

total_len = N_list[-1] - N_list[0]
total_interval = total_len // max_num
need_interval = total_interval - len(intervals)
print(need_interval)