def solution(my_strings, parts):
    answer = ''
    #enumerate함수를 사용하여 parts의 인덱스 값과 value값을 둘 다 들고온다.
    #i가 인덱스 j가 value값이다. my_strings의 i번째 string을 슬라이싱 하여 j[0]:j[1]+1번째
    #까지 answer에 저장한다.
    for i,j in enumerate(parts):
        answer += my_strings[i][j[0]:j[1]+1]
    return answer