from collections import Counter
T = int(input())
for _ in range(T):
    tc = int(input())
    tc_list = list(map(int, input().split()))
    counter = Counter(tc_list)
    most_value = counter.most_common(1)
    print(f'#{tc}', most_value[0][0])