def solution(num_str):
    answer = 0
    #map함수를 이용하여 문자열 형식의 num_str을 int형식으로 바꿔준다. 그 후 list형변환을 하여 
    #이터러블한 객체로 만들어서 sum함수를 이용하여 합을 구한다.
    answer = sum(map(int,num_str))
    return answer