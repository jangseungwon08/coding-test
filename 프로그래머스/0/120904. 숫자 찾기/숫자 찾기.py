def solution(num, k):
    answer = 0
    #정수형 num에 k가 있는 것을 알기 위해서 int형에서 str형으로 형 변환을 해준다.
    st_num = str(num)
    #형 변환 해준 st_num변수에 인덱스로 접근하기 위해서 range(len())함수를 사용하여 for문
    for i in range(len(st_num)):
        #자료형 맞춰주기 위해서 str(k)가 st_num[i]->value값과 같은 값을 찾으면
        if str(k) in st_num[i]:
            #인덱스에 +1한 값을 리턴
            return i+1
        #for문을 다 돌았는데 없으면 -1
    return -1