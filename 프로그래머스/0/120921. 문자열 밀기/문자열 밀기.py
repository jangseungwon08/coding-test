def solution(A, B):
    if A == B:  # A와 B가 처음부터 같으면 0
        return 0

    for i in range(1, len(A) + 1):  # 1부터 문자열 길이까지 반복
        A = A[-1] + A[:-1]  # A를 오른쪽으로 한 칸씩 밀기
        if A == B:
            return i  # i번 밀었을 때 B와 같아지면 i 반환

    return -1  # 끝까지 밀어도 같지 않으면 -1 반환
