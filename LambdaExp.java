import java.util.Arrays;
import java.util.List;

public class LambdaSort {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Bob", "Alice", "Charlie");
        names.sort((a, b) -> a.compareTo(b));
        System.out.println(names);
    }
}
