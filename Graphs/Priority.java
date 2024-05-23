import java.util.PriorityQueue;
import java.util.ArrayList;
import java.util.HashMap;

public class Priority {
    public static void main(String[] args) {
        PriorityQueue<Integer> arvore = new PriorityQueue<Integer>();
        HashMap<Integer, ArrayList<Integer>> vertices = new HashMap<Integer, ArrayList<Integer>>();

        arvore.add(40);
        vertices.put(40, new ArrayList<Integer>());

        vertices.get(40).add(2);

        arvore.add(40);

        vertices.get(40).add(4);

        System.out.println(arvore + " " + vertices.get(arvore.peek()));

        Integer custo = arvore.poll();

        System.out.println(custo + " " + vertices.get(custo).get(0));
        vertices.get(custo).remove(0);

        System.out.println(arvore + " " + vertices.get(arvore.peek()));

    }
}
