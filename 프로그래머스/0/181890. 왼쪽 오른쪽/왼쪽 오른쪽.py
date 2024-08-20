def solution(str_list):
    answer = []
    #str_list인덱스로 순회하면서
    for i in range(len(str_list)):
        #str_list의 i번째 인덱스 value값이 "l"일 때
        if str_list[i] == "l":
            #str_list리스트에서 i-1번째 까지 리턴
            return str_list[:i]
        # 'r'일 때
        elif str_list[i] == "r":
            #i+1번째 부터 끝까지 리턴
            return str_list[i+1:]
    #for문이 끝나면 빈 문자열 리턴 ( l이나 r이 없다는 뜻)
    return []