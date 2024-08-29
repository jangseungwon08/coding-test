def solution(picture, k):
    answer = []
    #picture 순회하면서
    for i in picture:
        #picture에 있는 변화된 각 문자열을 temp에 저장하기 위한 문자열
        temp = ''
        #picture에 있는 각 문자열 i를 순회하면서
        for j in i:
            #temp에 문자열에 있는 각 원소 j를 k번 곱해준 값을 각각 temp에 누적 저장
            temp += j*k
        #answer에 리스트로 만든 temp문자열을 k번 곱해서 answer에 누적 저장
        answer += [temp]*k
    return answer