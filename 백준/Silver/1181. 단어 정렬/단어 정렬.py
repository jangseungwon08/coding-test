import sys
input = sys.stdin.readline
N = int(input())
N_list = []
for _ in range(N):
    # readline으로 입력받으면 개행문자(\n)이 포함되기 때문에 
    # strip함수를 사용하여 한줄 씩 띄워지는 걸 방지
    # strip 매개변수가 생략되거나 None이면 char인자의 기본값은 
    # 공백을 제거하도록 한다.
    N_list.append(input().strip())
N_list = list(set(N_list))
# sort의 람다함수 x라 칭하고 x길이를 기준으로 오름차순하는데
# 길이가 같으면 사전순으로 오름차순 정렬
N_list.sort(key = lambda x:(len(x), x))

for i in N_list:
    print(i)