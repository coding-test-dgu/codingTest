package LimJH.개인문풀.소프티어;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class TreeAtack { //나무공격
    static int n;
    static int m;
    static List<Integer> destroyersCnt = new ArrayList<>();
    static List<List<Integer>> attackInfos = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        init();
        for(int attackOrder=0; attackOrder<2; ++attackOrder){
            List<Integer> attackInfo = attackInfos.get(attackOrder);
            for ( int i = attackInfo.get(0)-1; i<attackInfo.get(1); ++i){
                if(destroyersCnt.get(i) >0 ){
                    destroyersCnt.set(i, destroyersCnt.get(i) - 1);
                }
            }
        }

        System.out.println(destroyersCnt.stream().mapToInt(Integer::intValue).sum());
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; ++i) {
            st = new StringTokenizer(br.readLine());
            int cnt = 0;

            for (int j = 0; j < m; ++j) {
                int temp = Integer.parseInt(st.nextToken());

                if (temp == 1) {
                    cnt++;
                }
            }

            destroyersCnt.add(cnt);
        }

        // init attack info
        for(int i=0; i<2; ++i){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end =Integer.parseInt(st.nextToken());
            List<Integer> temp = new ArrayList<>(List.of(start, end));
            attackInfos.add(temp);
        }
    }
}
