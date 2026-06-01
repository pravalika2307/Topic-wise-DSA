def consecutive(arr):
    n = len(arr)
    cnt = 0
    maxi = 0
    for i in range(n):
        if arr[i] == 1:
            cnt += 1
            maxi = max(cnt, maxi)
        else:
            cnt = 0
    
    return maxi

arr= list(map(int, input().split()))
print(consecutive(arr))