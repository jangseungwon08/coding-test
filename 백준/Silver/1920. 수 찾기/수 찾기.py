n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int,input().split()))
n_list.sort()
def location(low,high):
    if low> high:
        return 0
    else:
        mid = (low+high) // 2
        if i == n_list[mid]:
            return 1
        elif n_list[mid] > i:
            return location(low, mid-1)
        else:
            return location(mid+1, high)
        
for i in m_list:
    print(location(0,n-1))
