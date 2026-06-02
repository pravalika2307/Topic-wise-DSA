def majority_element(arr):
    n = len(arr)
    major = n // 2
    for i in range(n):
        if arr.count(i) > major:
            return i
        
arr = list(map(int, input().split()))
print(majority_element(arr))