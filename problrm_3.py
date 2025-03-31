# def reverseArray(arr):
#     left=0
#     right=len(arr)-1

#     while left < right:
#         arr[left],arr[right]=arr[right],arr[left]

#         left+=1
#         right-=1

# if __name__=="__main__":
#     arr=[1,4,3,2,6,5]
#     reverseArray(arr)

#     for i in range (len(arr)):
#         print(arr[i],end=" ")



# Approch 2
def reversearray(arr):
    n=len(arr)

    for i in range(n//2):
        temp=arr[i]
        arr[i]=arr[n-1-i]
        arr[n-1-i]=temp          

if __name__=="__main__":
    arr=[1,4,3,2,6,5]
    reversearray(arr)

    for i in range (len(arr)):
        print(arr[i],end=" ")
