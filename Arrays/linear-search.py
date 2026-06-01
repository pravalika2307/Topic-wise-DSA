def linearsearch(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i

arr = list(map(int, input().split()))
target = int(input())
print(linearsearch(arr, target))
    
        