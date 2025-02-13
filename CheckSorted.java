public class CheckSorted {
    public static boolean isSorted(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i - 1]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        int[] sortedArr = {1, 2, 3, 4, 5};
        int[] unsortedArr = {5, 3, 8, 2};
        System.out.println(isSorted(sortedArr));  // Output: true
        System.out.println(isSorted(unsortedArr)); // Output: false
    }
}
