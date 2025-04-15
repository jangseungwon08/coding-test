import sys
input = sys.stdin.readline
# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
#N: 단어의 개수     M: 외울단어의 길이기준
N ,M = map(int ,input().split())
N_dict = {}
for _ in range(N):
    i = input().strip()
    if len(i) >= M:
        if i not in N_dict:
            N_dict[i] = 1
        else:
            N_dict[i] += 1
# 1번2번 기준은 내림차순으로 같은데 3번기준이 오름차순으로 다르다. 따라서 한꺼번에 람다에 넣어주고싶으면 -를 붙여주는 트릭을 사용한다.
# 1번기준: 내림차순 == -오름차순
# 2번기준: 내림차순 == -오름차순
# 3번기준: 오름차순
ans_dict = sorted(N_dict.items(), key = lambda x:(-x[1],-len(x[0]),x[0]))
for i, j in ans_dict:
    print(i)