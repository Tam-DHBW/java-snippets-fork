import java.util.HashMap;
import java.util.Map;

public class FibonacciMemoization {
    private static Map<Integer, Long> memo = new HashMap<>();

    public static void main(String[] args) {
        int n = 50; // Calculate the 50th Fibonacci number
        System.out.println("Fibonacci(" + n + ") = " + fibonacci(n));
    }

    // Fibonacci with memoization
    public static long fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        long result = fibonacci(n - 1) + fibonacci(n - 2);
        memo.put(n, result);
        return result;
    }
}