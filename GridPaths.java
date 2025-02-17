public class GridPaths {
    public static int countPaths(int m, int n) {
        if (m == 1 || n == 1) return 1; // Base case
        return countPaths(m - 1, n) + countPaths(m, n - 1); // Recursive case
    }

    public static void main(String[] args) {
        System.out.println("Paths in 3x3 grid: " + countPaths(3, 3));
    }
}
