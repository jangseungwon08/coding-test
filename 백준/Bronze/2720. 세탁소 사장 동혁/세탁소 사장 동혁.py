T = int(input())
#T만큼 순회하면서
for _ in range(T):
    #money를 정수형으로 받아옴
    money = int(input())
    #머니의 값이 1.24에서 124로 *100을 했으니 거스름돈c도 100을 곱해줘서
    #25 10 5 1로 나타냄
    for i in [25 , 10, 5 , 1]:
        #money에서 25를 정수형 나누기한 값을 출력
        print(money//i, end = ' ')
        #나누고 남은 돈을 계산하기위한 money%i값을 함
        money = money % i
