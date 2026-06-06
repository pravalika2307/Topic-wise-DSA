def peak_element(arr):

    n = len(arr)

    for i in range(n):
        if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
            return i
        
    return -1

arr = list(map(int, input().split()))
print(peak_element(arr))

