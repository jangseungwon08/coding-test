N = int(input())
ans = 0
wait_list = []
if N == 0:
    print(0)
    exit()
for _ in range(N):
    s_time, c_time = map(int, input().split())
    wait_list.append((s_time, c_time))
wait_list = sorted(wait_list, key = lambda x: x[0])
for current_time, task_time in wait_list:
    real_start_time = max(current_time , ans)
    real_finish_time = real_start_time + task_time
    ans = real_finish_time
print(ans)