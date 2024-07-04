'''
def solution(s):
    answer = ''
    #리스트 형식으로 담아줄 m을 구한다.
    m = []
    #s를 list형식으로 변환 후 for문 돌림
    for i in list(s):
        # 리스트 형식m에 list(s)의 각 원소 값들을 차레대로 넣어준다.
        m.append(i)
        #reverse = True를 선언하여 m을 내림차순으로 배치한다.
        m.sort(reverse = True)
        #그 후 answer에 join함수를 사용하여 str형식으로 변형하여준다.
        answer = ''.join(m)
    return answer
'''
#다른사람 풀이
#sorted함수는 list뿐 아니라 이터러블한 객체가 있으면 정렬가능하다. 
#따라서 Zbcdefg를 sorted로 내림차순 정렬하면 ["g","f","e","d","c","b","Z"]가 나오는데
#여기서 .join을 사용해서 문자열로 바꿔줘서"gfedcbZ"가 나온다..
def solution(s):
    answer = ''.join(sorted(s, reverse =  True))
    return answer
