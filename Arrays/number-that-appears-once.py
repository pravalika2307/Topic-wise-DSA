def appear_once(arr):
    n = len(arr)
    for i in range(n):
        if arr.count(i) == 1:
            return i

arr= list(map(int, input().split()))
print(appear_once(arr))