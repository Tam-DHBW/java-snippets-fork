import java.io.*;

public class FileWriterExample {
    public static void main(String[] args) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"))) {
            bw.write("Hello, Java!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
