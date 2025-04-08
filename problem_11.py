# Problem 11 :Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

# Note: It is guaranteed that the output fits in a 32-bit integer.

# MaxEnd and minEnd approach
def maxProduct(arr):
		# code here
	n=len(arr)
	curMin=arr[0]
	curMax=arr[0]
	maxProd=arr[0]
	for i in range(1,n):
		  #  we use temp variable to store maxvalue
		temp=max(arr[i],arr[i]*curMin,arr[i]*curMax)
		    
		curMin=min(arr[i],arr[i]*curMin,arr[i]*curMax)
		    
		curMax=temp
		    
		maxProd=max(maxProd,curMax)
		    
	return maxProd 


#Approach 2 :Traversing in bothe direction
# def maxProduct(arr):
#     n = len(arr)
#     maxProd = float('-inf')  
#     leftToRight = 1
#     rightToLeft = 1

#     for i in range(n):
#         if leftToRight == 0:
#             leftToRight = 1
#         if rightToLeft == 0:
#             rightToLeft = 1

#         leftToRight *= arr[i]
#         j = n - i - 1
#         rightToLeft *= arr[j]

#         maxProd = max(leftToRight, rightToLeft, maxProd)

#     return maxProd


if __name__== "main_":
    arr=[-2,6,-3,-10,0,2]
    print("Result" ,maxProduct(arr))