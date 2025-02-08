import java.util.Random;

public class RandomNumberExample {
    public static void main(String[] args) {
        Random random = new Random();
        int randomNumber = random.nextInt(100); // Random number between 0 and 99
        System.out.println(randomNumber);
    }
}
