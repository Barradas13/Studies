import java.util.Scanner;

public class Matriz {

    final static Scanner input = new Scanner(System.in);

    public static void imprimeMatriz(int[][] matriz){
        for (int i = 0; i < matriz.length; i ++) {
            for (int j = 0; j < matriz[0].length; j ++) {
                System.out.print(matriz[i][j] + " ");
            }System.out.println();
        }
    }

    //verifica apenas se tem o mesmo tamanho de linhas e colunas
    public static boolean verificarMatrizQuadrada(int[][] matriz){
        if(matriz.length == matriz[0].length){
            return true;
        }else{
            return false;
        }
    }

    //vai retornar em um vetor a soma dos valores do triangulo superior -> indice 0
    //e a soma do triangulo inferior -> indice 1, para assim o user ter já se ela é uma
    //triangular superior, inferior, ou facilitar o processo de verificação de identidade
    public static int[] somaTrianguloInfSup(int[][] matriz){
        int[] resultado = new int[2];
        
        int soma = 0;
        for(int i = 0; i < matriz.length; i ++){
            for(int j = i; j < matriz[0].length - 1; j ++){
                soma += matriz[i][j+1];
            }
        }

        resultado[0] = soma;

        soma = 0;

        for(int i = matriz.length - 1; i > 0; i --){
            for(int j = i; j > 0; j --){
                soma += matriz[i][j-1];
            }
        }

        resultado[1] = soma;

        return resultado;
    }

    //de acordo com os dados do somaTrianguloInfSup apenas verificará se todos os i = j são 1
    public static boolean verificarMatrizIdentidade(int[][] matriz, int[] superiores){
        if(superiores[0] == 0 && superiores[1] == 0){
            for(int i = 0; i < matriz.length; i ++){
                if(matriz[i][i] != 1){
                    return false;
                }
            }
            return true;
        }
        return false;
    }

    //percorre a matriz e verifica se todos os valores são 0
    public static boolean verificarMatrizNula(int[][] matriz){
        for(int i = 0; i < matriz.length; i ++){
            for(int j = 0; j < matriz[0].length; j ++){
                if(matriz[i][j] != 0){
                    return false;
                }
            }
        }
        return true;
    }

    //multiplica 2 vetores
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

    //faz a matriz transposta de B para assim ter como acessar os vetores colunas
    //percorre os vetores de A e B^t e multiplica-os para colocar os resultados
    public static int[][] multiplicarMatriz(int[][]matrizA, int[][] matrizB){
        int[][] transpostaB = matrizTransposta(matrizB);

        int[][] matrizC = new int[matrizA.length][transpostaB.length];
        
        int i = 0;
        int j = 0;
        while(j < matrizC[0].length && i != matrizC[0].length){
            matrizC[i][j] = multiplicaVetores(matrizA[i], transpostaB[j]);
            
            i ++;
            //se ja passou por todos os i com aquele j retorna i para um para passar com outro j
            if(i >= matrizC.length){
                i=0;
                j ++;
            }
        }

        return matrizC;
    }

    public static void main(String[] args) {
        int[][] matrizA = {{-1,3}, 
                          {4,2},};

        int[][] matrizB = {{1,2,}, 
                          {3,4,},};

        int[][] matrizC = multiplicarMatriz(matrizA, matrizB);
        imprimeMatriz(matrizC);
        
    }
}
