import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());
        int cross_count = 1;//대각선 칸 개수 : 1개부터 시작함
        int prev_cross_count = 0;//이전 대각선 칸의 개수 누적 합
        br.close();
        while (true) {
            // x가 전 대각선 칸의 누적 합 + 해당 대각선의 칸의 개수보다 작거나 같다는 뜻은 해당 대각선 칸에 x번째 분수가 존재한다는 것
            if (x <= prev_cross_count + cross_count) {
                if (cross_count % 2 == 1) {// 대각선의 개수가 홀수개라면
                    System.out.println((cross_count - (x - (prev_cross_count + 1))) + "/" + (x - prev_cross_count));
                    break;
                } else { // 짝수면
                    System.out.println((x - prev_cross_count) + "/" + (cross_count - (x - (prev_cross_count + 1))));
                    break;
                }
            } else { // x가 전 대각선 누적 합 + 현재 대각선 개수보다 크다면  두 변수의 합이 x보다 작다는 뜻이므로 해당 대각선에 없다는 것
                prev_cross_count += cross_count;//cross_count는 전 대각선이 되므로 누적으로 더해줌
                cross_count++;//대각선이 늘 때마다 1칸씩 늘어나므로 ++
            }
        }
    }
}