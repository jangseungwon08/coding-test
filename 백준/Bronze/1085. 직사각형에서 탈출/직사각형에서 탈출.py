x, y, w ,h = map(int,input().split())
least_dist = [x,w-x, y , h-y]
print(min(least_dist))