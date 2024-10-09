s = list()
#다섯줄의 입력이 주어진다
for _ in range(5):
    #2차원 배열로 입력받음
    s += [input()]
#바깥쪽 반복문 15번 반복 (단어의 길이가 15까지)
for j in range(15):
    #다섯줄의 입력이 주어졌기때문
    for i in range(5):
        #j가 s[i]의 길이 입력받은 단어길이보다 작으면 s[i][j]를 출력
        #j가 s의 인덱스 범위 안에있다는 뜻이므로
        if j < len(s[i]):
            print(s[i][j], end ='')