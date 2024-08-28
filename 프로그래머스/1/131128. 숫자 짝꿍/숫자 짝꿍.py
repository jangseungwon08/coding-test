'''
def solution(X, Y):
    answer = ''
    temp = []
    X, Y = sorted(list(X)), sorted(list(Y))
    for i in X[:]:  # X[:]를 사용해 X의 복사본으로 루프를 돌림
        if i in Y:
            temp += i
            X.remove(i)  # 첫 번째로 등장하는 i를 X에서 삭제
            Y.remove(i)  # 첫 번째로 등장하는 i를 Y에서 삭제
    temp.sort(reverse = True)
    if len(temp) == 0:
        return '-1'
    elif temp[0] == "0":
        return '0'
    else:
        return ''.join(temp)
'''
def solution(X, Y):
    # 문자열 X와 Y를 정렬된 리스트로 변환
    X = sorted(X)
    Y = sorted(Y)
    
    temp = []
    
    # 뒤에서부터 공통 요소를 찾기 위해 리스트를 뒤집음
    while X and Y:
        if X[-1] == Y[-1]:  # 공통 요소 발견
            temp.append(X.pop())  # 공통 요소를 temp에 추가하고, X와 Y에서 제거
            Y.pop()
        elif X[-1] > Y[-1]:  # X의 마지막 요소가 더 크면 X에서 제거
            X.pop()
        else:  # Y의 마지막 요소가 더 크면 Y에서 제거
            Y.pop()
    
    # 공통된 숫자가 없는 경우
    if not temp:
        return '-1'
    
    # 공통된 숫자 중 모두 0인 경우
    if temp[0] == '0':
        return '0'
    
    # 공통된 숫자를 내림차순으로 정렬하여 반환
    return ''.join(sorted(temp, reverse=True))
