#입력받을 문자열 개수
N = int(input())
#입력받을 문자열을 리스트 형식으로 초기화
N_list = list()
#N만큼 범위 순회하면서
for _ in range(N):
    #N_list에 input()값을 append해줌
    N_list.append(input())
#다 입력받고 중복제거를 위하여 set함수 사용하여 제거 하고 다시 list형식으로 변환
N_list = list(set(N_list))
#sorted함수 사용하여 N_list를 오름차순하는데 len(x)를 기준으로 먼저 하고 그
#뒤에는 x(사전순)를 기준으로 한다.
#여기서 lambda x는 익명함수를 정의 x는 각 원소를 가리킴
N_list = sorted(N_list, key = lambda x : (len(x), x))
#i를 출력
for i in N_list:
    print(i)