import java.util.Scanner;

public class Matriz3 {
    final static Scanner input = new Scanner(System.in);

    public static int multiplicaVetores(int[] linha, int[] coluna){
        int soma = 0;
        for (int i =0; i < linha.length; i ++) {
            soma += linha[i] * coluna[i];
        }

        return soma;
    }

    //inverte as linhas pelas colunas de uma matriz
    public static int[][] matrizTransposta(int[][] matriz){
        int[][] matrizReturn = new int[matriz[0].length][matriz.length];

        for(int i = 0; i < matrizReturn.length; i ++){
            for(int j =0; j < matrizReturn[0].length; j ++){
                matrizReturn[i][j] = matriz[j][i];
            }
        }

        return matrizReturn;
    }

    public static int[][] controiA(int n, int p, int q, int r, int x, int y){
        int[][] A = new int[n][n]; 
        
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < n; j ++){
                A[i][j] = (p * (i + 1) + q * (j + 1)) % x;
            }
        }

        return A;
    }

    public static int[][] controiB(int n, int p, int q, int r, int s, int x, int y){
        int[][] B = new int[n][n]; 
        
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < n; j ++){
                B[i][j] = (r * (i + 1) + s * (j + 1)) % y;
            }
        }

        return B;
    }

    public static void main(String[] args) {
        //Aij = (P × i + Q × j) (mod X)
        //Bij = (R × i + S × j) (mod Y)
        int n = input.nextInt();
        int p = input.nextInt();
        int q = input.nextInt();
        int r = input.nextInt();
        int s = input.nextInt();
        int x = input.nextInt();
        int y = input.nextInt();

        int[][] A = controiA(n, p, q, r, x, y);
        int[][] B = controiB(n, p, q, r, s, x, y);

        B = matrizTransposta(B);

        int f = input.nextInt();
        int m = input.nextInt();

        int resultado = multiplicaVetores(A[f - 1], B[m  - 1]);

        System.out.println(resultado);
    }
}

