

arr = [-13, 0, 6, 15, 16, 2, 15, -12, 17, -16, 0, -3, 19, -3, 2, -9, -6]
n = 17
k = 15


def func():
    res = 0
    dic = {}
    s = 0
    for i in range(n):
        s += arr[i]
        if (s) in dic:
            res = max(res, (i-dic[s-k])+1)
        if s not in dic:
            dic[s] = i
    print(dic)
    return res


print(func())
