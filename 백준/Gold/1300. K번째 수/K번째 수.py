N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N) 
    
    #이분탐색
    if cnt >= K: 
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)