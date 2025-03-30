import sys
input = sys.stdin.readline
N = int(input())
name_enter = dict()
for _ in range(N):
    name, enter = input().strip().split()
    name_enter[name] = enter
# 딕셔너리를 iterator에서 원소 삭제 시 list로 변경 후 진행
key_list = list(name_enter)
for k in key_list:
    if 'leave'== name_enter[k]:
        del name_enter[k]
#sorted사용 시 name_enter의 key값만 빠져나가기 때문에 괜찮음
res_list = sorted(name_enter, reverse = True)

for k in res_list:
    print(k)