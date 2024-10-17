N = int(input())
end_num = 666
N_list = []
count = 0
while True:
    if '666' in str(end_num):
        N_list.append(end_num)
        count += 1
    if count == N:
        break
    end_num += 1
print(N_list[count-1])