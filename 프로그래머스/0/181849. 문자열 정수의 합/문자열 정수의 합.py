def solution(num_str):
    answer = 0
    #map함수를 이용하여 문자열 형식의 num_str을 int형식으로 바꿔준다.
    #string은 이터러블한 객체이기때문에 sum함수를 이용하여 합을 구한다.
    answer = sum(map(int,num_str))
    return answer
