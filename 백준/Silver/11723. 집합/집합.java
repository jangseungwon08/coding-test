
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<Integer> set = new HashSet<>();
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i< n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String active = st.nextToken();
            if (active.equals("add")) {
                int num = Integer.parseInt(st.nextToken());
                set.add(num);
            } else if (active.equals("remove")) {
                int num = Integer.parseInt(st.nextToken());
                set.remove(num);
            } else if (active.equals("check")) {
                int num = Integer.parseInt(st.nextToken());
                sb.append(set.contains(num) ? 1 : 0).append("\n");
            } else if (active.equals("toggle")) {
                int num = Integer.parseInt(st.nextToken());
                if (set.contains(num)) set.remove(num);
                else set.add(num);
            } else if (active.equals("empty")) {
                set.clear();
            } else if (active.equals("all")) {
                set.clear();
                for (int j = 1; j <= 20; j++) {
                    set.add(j);
                }
            }
        }
        System.out.println(sb.toString());
    }
}