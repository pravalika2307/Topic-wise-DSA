def search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1

arr = list(map(int, input().split()))
target = int(input())
print(search(arr, target))
