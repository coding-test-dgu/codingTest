package LimJH.개인문풀.소프티어;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class GPTStyleNumberComparison {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>(){

            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) {
                    return o1[1]-o2[1];
                } else{
                    return o1[0]-o2[0];
                }
            }
        });

        for (int i = 0; i < N; ++i) {
            String[] now = br.readLine().split("\\.");
            int front;
            int back;
            if (now.length == 1) {
                front = Integer.parseInt(now[0]);
                back = -1;
            } else {
                front = Integer.parseInt(now[0]);
                back = Integer.parseInt(now[1]);
            }

            pq.add(new int[]{front, back});
        }

        StringBuilder sb = new StringBuilder();

        while (!pq.isEmpty()) {
            int[] now = pq.poll();

            if (now[1] != -1) {
                sb.append(now[0] + "." + now[1] + "\n");
            }else{
                sb.append(now[0]+"\n");
            }
        }

        System.out.println(sb.toString());
    }
}
