n_list = []
#수 10개를 입력받음
for _ in range(10):
    #각 줄에 입력받은 숫자를 n에 저장
    n = int(input())
    #n에 42를 나눈 나머지가 n_list에 없으면
    if n % 42 not in n_list:
        #n_list에 n %42의 값을 append시킴
        n_list.append(n%42)
#for문 순회 끝난 뒤 n_list길이 출력
print(len(n_list))