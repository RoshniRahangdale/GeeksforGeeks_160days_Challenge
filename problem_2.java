public class problem_2{
    public static void pushZeroToEnd(int[] arr) {
        int count = 0; // Position to place non-zero elements

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                // Swap arr[i] with arr[count]
                int temp = arr[i];
                arr[i] = arr[count];
                arr[count] = temp;
                count++;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 0, 4, 3, 0, 5, 0};
        pushZeroToEnd(arr);

        // Print result
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}

