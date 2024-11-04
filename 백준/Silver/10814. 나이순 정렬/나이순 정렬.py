N = int(input())
N_list = []
for _ in range(N):
    age, name = input().split()
    N_list.append((int(age), name))
#sorted함수를 사용하여 2차원인 N_list의 각 원소를 key를 lambda x로 설정하여
#x는 2차원 원소 안의 또 다른 리스트가 되어서 x[0]번째 즉 회원 나이에 대해서 비교하여
#오름차순 정렬
N_list = sorted(N_list, key= lambda x: x[0])
#N만큼 순회하면서
for i in range(N):
    #i번째 0번째(나이), i번째 1번째(이름)을 공백을 사이에 두고 출력
    print(N_list[i][0], N_list[i][1])