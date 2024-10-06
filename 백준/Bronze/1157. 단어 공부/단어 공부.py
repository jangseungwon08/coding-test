#문자열이 대소문자 구분없이 들어오기때문에 소문자로 받아들임
s = input().upper()
#문자열을 비교하기 위하여 set함수를 사용하여 중복 문자열 제거 후 리스트형식으로 변환
s_list = list(set(s))
#단어의 개수를 세는 리스트
count_list = []
#s_list순회하면서
for i in s_list:
    #s문자열에서 i문자의 개수를 세어 count에 저장
    count = s.count(i)
    #count_list에 구한 count값 append
    count_list.append(count)
    #count_list의 max(count_list)의 값이 1초과 즉 count_list의 최대 개수의 값이 중복이면
if count_list.count(max(count_list)) > 1:
    #?출력
    print('?')
    #max(count_list)의 값이 1 즉 count_list의 최대 개수가 1이면 즉 하나이면
else:
    #count_list에서의 최대값을 가지는 인덱스 값으로 s_list의 원소값을 구하여 대문자로 출력
    print(s_list[count_list.index(max(count_list))])