#입력값 정수형으로 나타내기 위해 int형변환
N = int(input())
#마지막에 'int'문자를 넣어주기 위해 'int'를 answer에 저장
answer = 'int'
#N//4만큼 반복함
for _ in range(N//4):
    #answer에 반복한 만큼 long 문자열을 더하고 마지막에 int 더함
    answer = 'long ' + answer
print(answer)