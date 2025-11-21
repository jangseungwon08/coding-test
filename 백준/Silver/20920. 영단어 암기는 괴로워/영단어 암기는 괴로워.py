import sys
input = sys.stdin.readline
N, M  = map(int, input().split())
word_dict = dict()
for _ in range(N):
    i = input().strip()
    if len(i) >= M:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1

ans_dict = sorted(word_dict.items(), key = lambda x:(-x[1],-len(x[0]),x[0]))
for i in ans_dict:
    print(i[0])