def union(arr1, arr2, n, m):
    n = len(arr1)
    m = len(arr2)
    for i in range(n):
        for j in range(m):
            a = arr1 + arr2
            a.sort()
    return list(set(a))

n = int(input())
m = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(union(arr1, arr2, n, m))
    

