# problem 4: Rotate the array

# Approach 1:Reversal Approach 
def rotateArr(arr,d):
    n=len(arr)

    d%=n
    reverse (arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)


def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]

        start +=1
        end -=1


if __name__=="__main__":
    arr=[1,2,3,4,5,6]
    d=3
    rotateArr(arr,d)
    for num in arr:
        print(num,end=" ")
                   