import sys
input = sys.stdin.readline
N = int(input())
result = 0
x = 1
# x의 제곱이 N보다 작거나 같을때 까지
#i의 스위치는 약수 개수만큼 눌리는데 숫자 i는 짝수 개 약수를 가짐
#--> 12 -> (1,12), (2,6), (3,4)...6개
#but i가 완전제곱수(1, 4, 9 ,16)이면 약수의 개수가 홀수이다.
# N이 10이면
# 완전제곱수 1,4,9를 찾으면 됨으로 3개가 나옴
while x* x <= N:
    x += 1
    result += 1
print(result)