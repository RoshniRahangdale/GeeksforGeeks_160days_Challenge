//Approach 1
// public class problem_3 {

//     public void reverseArray(int arr[]){
//         int left=0;
//         int right=arr.length-1;

//         while(left<right){
//             int temp;
//             temp=arr[left];
//             arr[left]=arr[right];
//             arr[right]=temp;

//             left++;
//             right--;

//         }
//     }
//     public static void main(String[] args) {
//         problem_3 obj=new problem_3();
//         int arr[]={1,4,3,2,6,5};
//         obj.reverseArray(arr);
//         for (int num:arr){
//             System.out.print(num+" ");
//         }
//     }

// }

//Approach 2

public class problem_3{

    public void reverseArray(int arr[]){
                int n=arr.length;
        
               for (int i=0;i<n/2;i++){
                 //swap
                 int temp=arr[i];
                 arr[i]=arr[n-i-1];
                 arr[n-i-1]=temp;
               }
            }
public static void main(String[] args) {
        problem_3 obj=new problem_3();
        int arr[]={1,4,3,2,6,5};
        obj.reverseArray(arr);

        for(int num:arr){
            System.out.print(num+" ");
        }
    }

}