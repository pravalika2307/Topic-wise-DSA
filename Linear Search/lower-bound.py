def lower_bound(arr, x):

    n = len(arr)

    for i in range(n):

        if arr[i] >= x:
            return i
        
    
    return n
        
arr = list(map(int, input().split()))
x = int(input())
print(lower_bound(arr, x))

