def moveZeroes(arr):
        pos = 0
        n = len(arr)
        for i in range(n):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1
        return arr
arr = list(map(int, input().split()))
print(*moveZeroes(arr))