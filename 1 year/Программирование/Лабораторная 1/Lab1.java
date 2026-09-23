public class Lab1 {
    public static double calculate(short ni, double xj) {
        return switch (ni) {
            case 1 -> Math.sin(Math.pow(Math.E, xj));
            case 3, 5, 7, 9, 10, 11, 12, 15, 18 -> Math.sin(Math.asin(Math.cos(xj)));
            default -> Math.asin(Math.pow(Math.pow(Math.cos(xj), 2), 2));
        };
    }

    public static void printMatrix(double[][] matrix) {
        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 12; j++) {
                System.out.printf("%7.3f", matrix[i][j]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        short[] n = new short[19];
        for (int i = 0; i < 19; i++) {
            n[i] = (short) (19 - i);
        }

        double[] x = new double[12];
        for (int i = 0; i < 12; i++) {
            x[i] = (Math.random() - 0.5) * 20;
        }

        double[][] d = new double[19][12];
        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 12; j++) {
                d[i][j] = calculate(n[i], x[j]);
            }
        }
        
        printMatrix(d);
    }
}
