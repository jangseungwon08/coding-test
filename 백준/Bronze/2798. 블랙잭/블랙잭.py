N, M = map(int,input().split())
N_list = list(map(int,input().split()))
total = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = N_list[i] + N_list[j] + N_list[k]
            if sum <= M:
                total.append(sum)
print(max(total))