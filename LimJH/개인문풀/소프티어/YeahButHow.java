package LimJH.개인문풀.소프티어;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class YeahButHow {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().replace("()","(1)").replace(")(", ")+(");
        System.out.println(input);
    }
}
