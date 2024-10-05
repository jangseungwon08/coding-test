#원래 체스의 개수 16개
chess_list = [1,1,2,2,2,8]
#입력받는 list개수를 list형식으로 만들어 n_list에 저장
n_list = list(map(int,input().split()))
#답을 위한 answer_list 리스트 선언
answer_list = []
#chess_list의 길이만큼 for문 순회하면서
for i in range(len(chess_list)):
    #chess_list의 i번째 인덱스 원소값이 n_list의 i번째 원소값 보다 크면
    #chess_list의 i 번째 인덱스 원소값에 n_list의 i번째 원소값을 빼서 
    #answer_list에 append(음수가 나와야됨)
    if chess_list[i] > n_list[i]:
        answer_list.append(chess_list[i] - n_list[i])
    #chess_list의 원소값이 n_list의 원소값보다 작거나 같으면
    else:
        #answer_list에 chess_list의 i번째 와 n_list의 i번째에 append
        answer_list.append(chess_list[i] - n_list[i])
        #answer_list순회하면서 i 출력 end함수를 사용하여 공백을 두고 출력 
for i in answer_list:
    print(i, end = ' ')