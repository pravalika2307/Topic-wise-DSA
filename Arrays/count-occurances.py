def occurances(arr, x):

    n = len(arr)

    for i in range(n):
        if i == x:
            return arr.count(i)

    return -1

arr = list(map(int, input().split()))
x = int(input())
print(occurances(arr, x))