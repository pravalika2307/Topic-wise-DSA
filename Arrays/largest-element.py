def islargest(arr):
    for i in range(len(arr)):
        return max(arr) 
arr = list(map(int, input().split()))
print(islargest(arr))