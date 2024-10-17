###삼각형 성질을 이용하여 작은 두변의 길이합이 가장 큰 변의 길이보다 커야된다.
tri_list = list(map(int,input().split()))
tri_list.sort()
if tri_list[0] + tri_list[1] > tri_list[2]:
    print(sum(tri_list))
elif tri_list[0] + tri_list[1] <= tri_list[2]:#작은 두 변의 길이가 
    #가장 큰 변의 길이보다 크거나 같으면
    tri_list[2] = tri_list[0]+ tri_list[1] -1#
    print(sum(tri_list))