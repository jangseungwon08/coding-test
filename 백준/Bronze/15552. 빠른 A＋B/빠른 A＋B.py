#sys.stdin.readline()함수를 사용하기 위한 sys임포트
import sys
#첫줄에 정수형 테스트케이스 개수 T
T = int(input())
#T범위 순회하면서
for i in range(T):
    #input대신 sys.stdin.readline사용하여 입력 받은 문자열을 공백 기준으로 나눔
    a, b = map(int, sys.stdin.readline().split())
    #a와 b출력
    print(a+b)