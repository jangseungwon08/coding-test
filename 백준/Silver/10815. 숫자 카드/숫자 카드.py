#상근이가 가지고있는 숫자 카드의 개수
N = int(input())
#검색연산이 많아지기 때문에 N_list에 set(집합)을 사용 따라서 O(1)의 시간복잡도가 걸려서
#시간복잡도 감소
N_list = set(map(int,input().split()))
#M개의 숫자
M = int(input())
#상근이가 가지고있는 숫자인지 아닌지 구분하는 list
M_list = list(map(int,input().split()))
#M개의 수에 대해서니까 M_list의 길이 만큼 [0]을 곱해서 ans_list에  저장
ans_list = []
#N_list순회하면서
for i in M_list:
    #M_list에 i의 원소값이 있으면
    if i in N_list:
        ans_list.append(1)
    else:
        ans_list.append(0)
#순회다하고 ans_list출력
for i in ans_list:
    print(i, end = ' ')