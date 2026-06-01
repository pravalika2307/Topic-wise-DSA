def removeDuplicates(arr):
        if not arr:
            return 0
        write_index = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                arr[write_index] = arr[i]
                write_index += 1            
        return write_index
arr = list(map(int, input().split()))
arr.sort()
print(removeDuplicates(arr))