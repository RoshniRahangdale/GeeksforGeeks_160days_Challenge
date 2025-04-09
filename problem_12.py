# problem 12 :
# Max Circular Subarray Sum
# Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

def circularSubarraySum(arr):
    totalSum=0
    currMaxSum=0
    currMinSum=0
    maxSum=arr[0]
    minSum=arr[0]
    
    for i in range (len(arr)):
        # find max sum subarray
        currMaxSum=max(currMaxSum+arr[i],arr[i])
        maxSum=max(currMaxSum,maxSum)
        # fing min sum subarray
        currMinSum=min(currMinSum+arr[i],arr[i])
        minSum=min(minSum,currMinSum)
        
        totalSum+=arr[i]
        
    normalSum=maxSum
    circularSum=totalSum-minSum
    
    # if min subarray and total sum of array is same then return normalSum
    if minSum==totalSum:
        return normalSum
    
    return max(normalSum,circularSum)

if __name__== "__main__":
    arr=[8,-8,9,-9,10,-11,12]
    print(circularSubarraySum(arr))
