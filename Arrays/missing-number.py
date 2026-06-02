def missing_number(arr):
    n = len(arr) + 1
    totalSum = sum(arr)
    expSum = n * (n + 1) // 2
    return expSum - totalSum

arr = list(map(int, input().split()))
print(missing_number(arr))
