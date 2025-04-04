def findMajority(arr):
    n = len(arr)
    freq = {}
    res = []

    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1

    for ele, cnt in freq.items():
        if cnt > n // 3:
            res.append(ele)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]  

    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end=" ")
