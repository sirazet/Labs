public class Lab1 {
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
                if (n[i] == 1) {
                    d[i][j] = Math.sin(Math.pow(Math.E, x[j]));
                }
                else if (java.util.List.of(3, 5, 7, 9, 10, 11, 12, 15, 18).contains((int) n[i])) {
                    d[i][j] = Math.sin(Math.asin(Math.cos(x[j])));
                }
                else {
                    d[i][j] = Math.asin(Math.pow(Math.pow(Math.cos(x[j]), 2), 2));
                }
            }
        }
        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 12; j++) {
                System.out.printf("%7.3f", d[i][j]);
            }
            System.out.println();
        }
    }
}
