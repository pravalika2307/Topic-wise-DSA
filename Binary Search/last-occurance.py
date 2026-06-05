def last_occurrence(arr, target):

    n = len(arr)

    for i in range(n-1, -1, -1):
        if arr[i] == target:
            return i
    return -1

arr = list(map(int, input().split()))
target = int(input())
print(last_occurrence(arr, target))