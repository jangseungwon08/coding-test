from collections import Counter
S = input()
N = int(input())
for _ in range(N):
    alpha, s_idx, e_idx = input().split()
    s_idx, e_idx = int(s_idx), int(e_idx)
    sub_string = S[s_idx:e_idx+1]
    ans_dict = Counter(sub_string)
    ans = ans_dict[alpha]
    print(ans)