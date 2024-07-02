def solution(s):
    answer = True
    #(s의길이가 4또는 6일때) 그리고 s가 숫자로만 이루어져있는지 알 수 있는
    #str메서드에서 사용가능한 isdigit함수를 사용해서 4또는 6을 만족하고 숫자로만 이루어져 있으면
    #true반환
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True
    else:
        answer = False
    return answer
