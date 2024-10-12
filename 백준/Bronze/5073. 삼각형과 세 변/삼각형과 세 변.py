while True:
    n_list = list(map(int, input().split()))
    n_list.sort()
    if sum(n_list) == 0:
        break
    if n_list.count(max(n_list)) == 3:
        print('Equilateral')
    elif max(n_list) < n_list[0] + n_list[1] and (n_list[0] == n_list[1] or n_list[1] == n_list[2] or n_list[0] == n_list[2]):
        print('Isosceles')
    elif max(n_list) < n_list[0] + n_list[1] and (n_list[0] != n_list[1] != n_list[2]):
        print('Scalene')
    else:
        print('Invalid')