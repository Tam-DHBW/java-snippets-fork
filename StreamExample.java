import java.util.Arrays;
import java.util.List;

public class StreamExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(3, 7, 2, 8, 1, 9);
        numbers.stream()
               .filter(n -> n % 2 == 0)
               .forEach(System.out::println); // Print even numbers
    }
}
