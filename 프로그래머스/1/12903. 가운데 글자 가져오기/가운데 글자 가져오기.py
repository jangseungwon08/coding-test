def solution(s):
    answer = ''
    if len(s) % 2:
        n = [s[(len(s) // 2)]]
        answer = ''.join(n)
    else:
        n = [s[(len(s)//2) - 1], s[len(s) // 2]]
        answer = ''.join(n)
    return answer