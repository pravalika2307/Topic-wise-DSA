def sums(arr):
    arr = sorted(arr)
    return arr

arr = list(map(int, input().split()))
print(*sums(arr))