N = int(input())
N_list = list(map(int,input().split()))
max_score = max(N_list)
new_score = 0
for i in N_list:
    new_score += (i / max_score)*100
print(new_score/len(N_list))