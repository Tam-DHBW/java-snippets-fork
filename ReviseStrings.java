public class ReverseString {
    public static String reverse(String str) {
        if (str.isEmpty()) return str; // Base case
        return reverse(str.substring(1)) + str.charAt(0); // Recursive case
    }

    public static void main(String[] args) {
        System.out.println("Reverse of 'hello': " + reverse("hello"));
    }
}
