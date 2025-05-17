package LimJH.개인문풀.백준;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P6236_이분탐색_재풀이하기 {
    //SSAFY지원🔥🔥🔥🔥

    static int N,M;
    static List<Integer> expenses = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());


        for (int i = 0; i < N; i++) {
            expenses.add(Integer.parseInt(br.readLine()));
        }

        System.out.println(binarySearch());
    }

    private static int binarySearch() {
        int start = expenses.stream().mapToInt(Integer::intValue).max().getAsInt();
        int end = expenses.stream().mapToInt(Integer::intValue).sum();
        int K = 0;
        while (start <= end) {
            int mid = (start+end)/2; // mid is k (;candidate k)
            if (isPossible(mid)) { //mid원으로 M번꺼내서 N일커버 가능
                K = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return K;
    }

    // candidateK원으로 N일동안 M번 꺼내서 사용가능한지 check
    private static boolean isPossible(int candidateK) {
        int currentCash = candidateK;
        int withdrawCnt = 1;

        for (int i = 0; i < N; ++i) {

            if (expenses.get(i) > currentCash) {
                withdrawCnt++;
                currentCash = candidateK;
            }

            currentCash-= expenses.get(i);
        }

        return withdrawCnt<=M;
    }
}
