
def func(n, arr):
    m = arr[n-1]
    res = []
    for i in range(n-1, -1, -1):
        m = max(m, arr[i])
        if arr[i] >= m:
            res.append(arr[i])
    return res[::-1]


func(6, [16, 17, 4, 3, 5, 2])
