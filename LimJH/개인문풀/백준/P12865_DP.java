package LimJH.개인문풀.백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*

 */
public class P12865_DP {
    static int N, K;
    static int[] w = new int[101];
    static int[] v = new int[101];
    static int[][] dp = new int[101][100_001]; // 사용메모리 : 101 * 십만 * 4 ~= 40MB


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            w[i] = Integer.parseInt(st.nextToken());
            v[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= K; ++j) {
                dp[i][j] = dp[i-1][j];
                if (j - w[i] >= 0) {// 현재 가방 무게가 항상 내가 선택한 무게보다 큰 경우에만 업데이트
                    dp[i][j] = Math.max(dp[i - 1][j], v[i] + dp[i - 1][j - w[i]]);
                }
            }

        }

        System.out.println(dp[N][K]);

    }


}
