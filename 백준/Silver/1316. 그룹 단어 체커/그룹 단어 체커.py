N = int(input())
count = N
#N만큼 순회하면서
for _ in range(N):
    #문자열 입력받아 s에 저장
    s = input()
    #s의 i+1번째 문자열을 검색하기 위해서 len(s)의 -2번째 까지 순회
    for i in range(len(s)-1):
        #s의 i번째 문자열과 i+1번째 문자열이 같으면 아래 코드 무시하고 다음 i로 jump
        if s[i] == s[i+1]:
            continue
        # s[i]의 원소값이 s[i+1]번째 원소값부터 마지막 까지에 값이 존재하면 
        #연속되 그룹단어가 아니기때문에 
        elif s[i] in s[i+1:]:
            #count에 -1 누적 빼고 break
            count -= 1
            break
print(count)