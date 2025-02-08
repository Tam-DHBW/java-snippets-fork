public class MergeSort {
  public static int[] mergeSort(int[] array) {
    if (array.length < 2) {
      return array;
    }

    int midpoint = array.length / 2;
    System.out.println(midpoint);

    int[] left = Arrays.copyOfRange(array, 0, midpoint);
    int[] right = Arrays.copyOfRange(array, midpoint, array.length);
    return merge(mergeSort(left), mergeSort(right));
  }

  public static void main(String[] args){
    int[] array = {38, 27, 43, 3, 9, 82, 10};

    int[] sortedArray = mergeSort(array);
    System.out.println(sortedArray);
  }
}