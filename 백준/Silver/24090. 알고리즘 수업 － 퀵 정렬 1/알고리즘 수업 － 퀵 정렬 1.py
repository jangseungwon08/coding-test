import sys
sys.setrecursionlimit(int(1e4)) 
input = sys.stdin.readline
N, K = map(int, input().split())
A_list = list(map(int, input().split()))
count = 0

def quicksort(A_list,low, high):
    if low < high:
        pivotpoint = partition(A_list, low, high)
        quicksort(A_list,low, pivotpoint - 1)
        quicksort(A_list, pivotpoint+1, high)

def partition(A_list, low, high):
    global count
    x = A_list[high]
    i = low - 1
    for j in range(low, high):
        if A_list[j] <= x:
            i += 1
            A_list[i], A_list[j] = A_list[j], A_list[i]
            count += 1
            if count == K:
                print(A_list[i], A_list[j])
    if i +1 != high:
        A_list[i+1] , A_list[high] = A_list[high], A_list[i+1]
        count += 1
        if count == K:
            print(A_list[i+1], A_list[high])
    return i+1

quicksort(A_list, 0, len(A_list)-1)
if count < K:
    print(-1)