import sys
# 입력 속도 향상
input = sys.stdin.readline

a, k = map(int, input().split())
a_list = list(map(int, input().split()))
count = 0
k_element = -1
tmp = [0] * a 

def mergesort(s, e): # (시작 인덱스, 끝 인덱스)
    global count, k_element
    if s < e:
        mid = (s + e) // 2
        mergesort(s, mid)       # 전반부 정렬
        mergesort(mid + 1, e)   # 후반부 정렬
        merge(s, mid, e)      # 병합

def merge(s, mid, e):
    global count, k_element

    # k번째 값을 이미 찾았다면, 더 이상 병합 작업을 수행할 필요가 없습니다.
    if k_element != -1:
        return
    
    i = s       # 왼쪽 배열 포인터
    j = mid + 1 # 오른쪽 배열 포인터
    t = 0       # tmp 배열의 포인터

    # [수정된 부분 1] 올바른 루프 조건
    while i <= mid and j <= e:
        if a_list[i] <= a_list[j]:
            tmp[t] = a_list[i]
            i += 1
        else:
            tmp[t] = a_list[j]
            j += 1
            
        # tmp에 값을 "저장"할 때마다 count 증가
        count += 1
        if count == k:
            k_element = tmp[t]
        t += 1

    # [수정된 부분 2] 왼쪽 배열이 남은 경우 (올바른 루프 조건)
    while i <= mid:
        tmp[t] = a_list[i]
        i += 1
        count += 1
        if count == k:
            k_element = tmp[t]
        t += 1
        
    # [수정된 부분 3] 오른쪽 배열이 남은 경우
    while j <= e:
        tmp[t] = a_list[j]
        j += 1
        count += 1
        if count == k:
            k_element = tmp[t]
        t += 1

    # tmp에 정렬된 값을 원본 a_list에 다시 복사
    i = s
    t = 0
    while i <= e:
        a_list[i] = tmp[t]
        i += 1
        t += 1

mergesort(0, a - 1)
print(k_element)