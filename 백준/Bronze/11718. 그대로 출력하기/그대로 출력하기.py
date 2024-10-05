#무한반복문으로
while True:
    #try함수를 사용하여 일단 print()안에 문을 실행
    try:
        #문자열을 입력받음
        print(input())
        #EOFError는 예외처리로 end of file의 줄임말로 입력값이 없어지는 상황
    except EOFError:
        #프로그램 종료
        break