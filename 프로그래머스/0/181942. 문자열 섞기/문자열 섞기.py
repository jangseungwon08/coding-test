def solution(str1, str2):
    answer = ''
    #str1과 str2의 길이가 같다고 했으니 str1기준으로 index접근
    for i in range(len(str1)):
        #answer에 str1[i]번째 문자열과 str2[i]번째 문자열을 합친 문자열을 answer에 저장
        answer += str1[i] + str2[i]
    return answer