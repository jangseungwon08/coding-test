def solution(my_string, queries):
    answer = ''
    #쿼리 순회하면서 s와 e를 추출
    for s,e in queries:
        #my_string의 s-1까지 문자열 추출
        #my_string의 s부터 e까지 구간의 서브스트링 추출한 뒤 뒤집음
        #my_string의 e+1부터 끝까지
        #이 로직은 my_string[s:e+1][::-1]의 부분에서 핵심이다. 따라서 쿼리 순회하면서 이 부분만           문자열이 뒤집어진 채로 my_string에 계속 저장됨
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string