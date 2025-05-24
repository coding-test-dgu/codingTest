package LimJH.개인문풀.백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P12865_DP_틀림_with_DFS {
    static int N,K;
    static int[][] products;
    static boolean[] visited;
    static int answer = 0;
    public static void main(String[] args) throws IOException {

        // inputs initialization
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        products = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            products[i][0] = Integer.parseInt(st.nextToken()); // w
            products[i][1] = Integer.parseInt(st.nextToken()); // v
        }

        dfs(0, 0, 0);
        System.out.println(answer);

    }

    private static void dfs(int idx, int valueSum, int weightSum) {
        if (weightSum > K) {
            return ;
        }

        if (idx == N) { // 모든 아이템 탐색 했으면
            answer = Math.max(answer, valueSum);
            return ;
        }

        dfs(idx+1, valueSum, weightSum);
        dfs(idx + 1,  valueSum + products[idx][1], weightSum + products[idx][0]);


    }
}
