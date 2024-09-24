#map함수를 사용하여 input()을 공백을 기준으로 나눈 문자열을 int형식으로 형 변환
n, x = map(int, input().split())
#map함수를 사용하여 공백을 기준으로 나눈 문자열을 int형식으로 구성된 list로 변환
n_list = list(map(int, input().split()))
#n_list순회하면서 입력받은 x가 i보다 크면 i출력 end = ' '을 사용하여 개행하지 않고 한줄로 출력
for i in n_list:
    if x > i:
        print(i, end = ' ')