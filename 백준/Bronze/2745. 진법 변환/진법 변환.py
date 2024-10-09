# 진법 변환을 위한 num_list 생성
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# a는 b진법으로 표현되는 문자열을 입력받고 b는 n을 입력받음
a, b = input().split()
# 최종 합을 위한 sum 변수
sum = 0
# len(a)-1 부터 (-1+1) 까지 -1만큼 감소시키면서
for i in range(len(a)):
    # a의 i번째 인덱스 원소값을 num_list의 몇번째 인덱스에 있는지 확인
    idx = num_list.index(a[i])
    # 인덱스 값 * b의 수에 (len(a)-1-i)의 자리수를 제곱하여 곱해줌
    ivt = (idx) * (int(b)**(len(a)-1-i))
    # sum에 ivt변수를 더해준다
    sum += ivt
# sum출력
print(sum)