spot_list = []
for _ in range(3):
    spot_list += list(map(int,input().split()))
x_list = spot_list[::2]
y_list = spot_list[1::2]
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]
print(x, y)