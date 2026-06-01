def rotate(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

arr = list(map(int, input().split()))
k = int(input())
arr = rotate(arr, k)
print(*arr)