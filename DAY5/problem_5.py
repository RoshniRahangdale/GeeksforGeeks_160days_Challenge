def nextPermutation( arr):
        # code here
    n=len(arr)
       
    pivot =-1
       
    #   to find pivot
    for i in range (n-2,-1,-1):
           if arr[i]<arr[i+1]:
               pivot=i
               break
           
        # if array is in descending order 
    if pivot==-1:
            arr.reverse()
            return arr
        
        # fing rightmost greater element that pivot
    for i in range(n-1,pivot,-1):
            if arr[i]>arr[pivot]:
                arr[i],arr[pivot]=arr[pivot],arr[i]
                break
                
    left ,right=pivot+1,n-1
    while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    

if __name__=="__main__":
    arr=[62,92,96,43,28,37,92,5,3,54,93,83,22]
    nextPermutation(arr)
    for num in arr:
        print(num,end=" ")        
        # 62 92 96 43 28 37 92 5 3 83 22 54 93
