def second_largest(arr):
    for i in range(len(arr)):
        a = sorted(arr)
    return a[-2]
    
arr = list(map(int, input().split()))
print(second_largest(arr))