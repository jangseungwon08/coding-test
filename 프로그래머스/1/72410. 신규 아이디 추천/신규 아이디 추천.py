def solution(new_id):
#     1단계: 모든 대문자 소문자로 변경
    temp  = new_id.lower()
#     2단계: 소문자 숫자 - _ . 제거
    temp = [i for i in temp]
    for i in temp.copy():
        if i.isdigit() or i.isalpha() or i == '-' or i =='_' or i == '.':
            continue
        else:
            temp.remove(i)
#     3단계: 마침표(.)이 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    three_temp = []
    for i in temp:
        if three_temp and i == '.' and three_temp[-1] == '.':
            continue
        else:
            three_temp.append(i)
    temp = three_temp
#     4단계: 마침표가 처음이나 끝에 위치하면 제거
    if temp[0] == '.':
        temp.pop(0)
    if temp and temp[-1] == '.':
        temp.pop()
#     5단계: 빈 문자열이라면 new_id에 'a'대입
    if len(temp) == 0:
        temp.append('a')
#     6단계: 길이가 16자 이상이면 처음 15개 문자를 제외한 모든 문자 제거 후 
            # 마침표(.)가 끝에 위치하면 마침표 제거
    if len(temp) >= 16:
        temp = temp[:15]
        if temp[-1] == '.':
            temp.pop()
#     7단계: new_id의 길이가 2자 이하면 마지막 문자를 new_id의 길이가 3이 될 때 까지 붙임
    if len(temp) <= 2:
        while len(temp) != 3:
            temp.append(temp[-1])
    answer = ''.join(temp)
    return answer