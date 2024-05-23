import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayList;

public class Grafo {
    final static Scanner Sc = new Scanner(System.in);

    public static void main(String[] args) {
        HashMap<Integer, ArrayList<Integer>> grafoRecebido = new HashMap<>();
        grafoRecebido = lerGrafo(Sc.nextInt(), Sc.nextInt());
        imprimirGrafo(grafoRecebido);
    }

    public static void imprimirGrafo( HashMap<Integer, ArrayList<Integer>> grafo) {
        for (Integer i : grafo.keySet()) {
            System.out.println(i + " " + grafo.get(i));
        }
    }

    public static HashMap<Integer, ArrayList<Integer>> lerGrafo(int v, int a) {
        HashMap<Integer, ArrayList<Integer>> grafoEnviar = new HashMap<>();
        
        for (int i = 1; i < v + 1; i++) {
            grafoEnviar.put(i, new ArrayList<Integer>());
        }

        for (int i = 0; i < a; i++) {
            int n1 = Sc.nextInt();
            int n2 = Sc.nextInt();

            grafoEnviar.get(n1).add(n2);
            grafoEnviar.get(n2).add(n1);

        }

        return grafoEnviar;
    }
}
