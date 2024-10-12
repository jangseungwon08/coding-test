N = int(input())
N_list = []
x_list , y_list = list(), list()
#N_list로 x y 좌표를 N개만큼 입력받아
for _ in range(N):
    N_list +=  list(map(int,input().split()))
#x부분은 0부터 2칸씩 띄우는 값이니 두칸씩 띄어서 x_list에 append
for i in range(0,len(N_list), 2):
    x_list.append(N_list[i])
#y부분은 1부터 2칸씩 띄우는 값이니 홀수값으로만 y_list에 append
for j in range(1,len(N_list), 2):
    y_list.append(N_list[j])
#x_list의 max값 - min값 * y_list의 max값 - min값을 곱한 값을 출력
print((max(x_list) - min(x_list)) * (max(y_list)-min(y_list)))