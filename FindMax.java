public class FindMax {
    public static int findMax(int[] arr) {
        int max = arr[0];
        for (int num : arr) {
            if (num > max) max = num;
        }
        return max;
    }

    public static void main(String[] args) {
        int[] arr = {4, 7, 1, 9, 2};
        System.out.println("Max: " + findMax(arr));
    }
}
