def maxSubarraySum(arr):
    res=arr[0]
    maxEnding=arr[0]

    for i in range (1,len(arr)):
        maxEnding=max(maxEnding+arr[i],arr[i])

        res=max(maxEnding,res)

    return res

if __name__== "__main__":
    arr=[2,3,-8,7,-1,2,3]
    print("Result :",maxSubarraySum(arr))