N = int(input())
count = 0
N_list = list(map(int,input().split()))
for i in N_list:
    #N_list의 원소값 i 를 소수는 1을 제외한 자기자신이니 
    #2부터 i까지 i에 j를 나눈 나머지가 0, i가 j와 같으면
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                count += 1
            break
print(count)