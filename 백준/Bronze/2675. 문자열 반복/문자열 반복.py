#테스트케이스 개수 T를 입력받음
T = int(input())
#T범위까지 순회하면서 
for _ in range(T):
    #r과 s를 t개수 만큼 입력받음
    R, S = input().split()
    #입력받은 문자열s 순회하면서
    for i in S:
        #변수 r을 정수형으로 각 i의 문자열을 곱하여 개행하지않고 연속으로 출력
        print(int(R) * i, end = '')
        #한칸 띄우기 위한 print공백
    print()