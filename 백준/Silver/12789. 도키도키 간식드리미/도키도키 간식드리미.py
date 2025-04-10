import sys
input = sys.stdin.readline
N = int(input())
students = list(map(int,input().split()))
stack = []
# 현재 넘버 
now = 1

# 번호표 순회하면서
for student in students:
    # 하나씩 stack에 append시킴
    stack.append(student)

    # stack에 원소가 존재하고 stack의 top이 현재값과 같으면 stack pop하고 now 1더함
    while stack and stack[-1] == now:
        stack.pop()
        now += 1

if stack:
    print("Sad")
else:
    print("Nice")