import java.util.Scanner;
import java.util.PriorityQueue;
import java.util.ArrayList;
import java.util.HashMap;

public class Djikstra {
    final static Scanner Sc = new Scanner(System.in);
    

    public static HashMap<Integer, ArrayList<int[]>> lerGrafo(int v, int a) {
        HashMap<Integer, ArrayList<int[]>> grafoEnviar = new HashMap<>();
        
        for (int i = 1; i < v + 1; i++) {
            grafoEnviar.put(i, new ArrayList<int[]>());
        }

        for (int i = 0; i < a; i++) {
            int n1 = Sc.nextInt();
            int n2 = Sc.nextInt();
            int custo = Sc.nextInt();

            int[] v1 = {n2, custo};
            int[] v2 = {n1, custo};

            grafoEnviar.get(n1).add(v1);
            grafoEnviar.get(n2).add(v2);

        }

        return grafoEnviar;
    }

    public static int djikstra(HashMap<Integer, ArrayList<int[]>> grafo, int origem, int destino){
        int[] distancia = new int[grafo.size()];
        int[] pais = new int[grafo.size()];
        boolean[] ja_foi = new boolean[grafo.size()];


        for(int i = 0; i < distancia.length; i ++){
            distancia[i] = Integer.MAX_VALUE / 2;
            pais[i] = -1;
        }

        distancia[origem - 1] = 0;
        pais[origem - 1] = -1;

        PriorityQueue<Integer> candidatos = new PriorityQueue<Integer>();
        HashMap<Integer, ArrayList<Integer>> verticesCandidatos = new HashMap<Integer, ArrayList<Integer>>();
        candidatos.add(0);
        verticesCandidatos.put(0, new ArrayList<Integer>());

        verticesCandidatos.get(0).add(origem);

        while (candidatos.size() > 0) {
            Integer valorU = candidatos.poll();
            Integer u = verticesCandidatos.get(valorU).get(0);
            verticesCandidatos.get(valorU).remove(0);

            System.out.println(u);

            for (int[] i : grafo.get(u)) {
                if(! ja_foi[i[0] -1]){
                    if(distancia[i[0] - 1] > valorU + i[1]){
                        distancia[i[0] - 1] = valorU + i[1];
                        pais[i[0] - 1] = u;

                        candidatos.add(distancia[i[0] - 1]);

                        if(verticesCandidatos.get(distancia[i[0]-1]) != null){
                            verticesCandidatos.get(distancia[i[0]-1]).add(i[0]);
                        }else{
                            verticesCandidatos.put(distancia[i[0]-1], new ArrayList<Integer>());
                            verticesCandidatos.get(distancia[i[0]-1]).add(i[0]);
                        }

                    }
                }

                ja_foi[u -1] = true;

            }
        }

        return distancia[destino - 1];
        
    }

    public static void main(String[] args) {
        // Exemplo de entrada para o grafo
        // qtd_v qtd_a
        // a - b custo_x
        //
        // 5 4
        // 1 2 10
        // 3 4 15
        // 5 1 2
        // 4 2 23
        // 1 3 (quero saber o menor caminho do 1 para o 3)

        int v = Sc.nextInt();
        int a = Sc.nextInt();

        HashMap<Integer, ArrayList<int[]>> grafo = lerGrafo(v, a);

        int origem = Sc.nextInt();
        int destino = Sc.nextInt();

        int menor_caminho_custo = djikstra(grafo, origem, destino);

        System.out.println(menor_caminho_custo);

    }
}
