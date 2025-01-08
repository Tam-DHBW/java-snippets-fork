public class BinarySearch {
    public static int binarySearch(int[] arr, int left, int right, int target) {
        if (left > right) return -1;
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        return arr[mid] > target 
            ? binarySearch(arr, left, mid - 1, target) 
            : binarySearch(arr, mid + 1, right, target);
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 5, 8};
        int target = 5;
        int index = binarySearch(arr, 0, arr.length - 1, target);
        System.out.println("Found at index: " + index);
    }
}
