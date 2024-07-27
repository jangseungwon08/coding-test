def solution(my_string, s, e):
    #my_string[:s]는 s-1번째 인덱스 까지
    #my_string[s:e+1][::-1]은 my_string s부터 e까지 접근하고 그 슬라이싱 한 문자열에서
    #역순으로 출력 
    #my_string[e+1:]은 e+1번째 인덱스부터 끝까지
    answer = my_string[:s]+ my_string[s:e+1][::-1] + my_string[e+1:]
    return answer