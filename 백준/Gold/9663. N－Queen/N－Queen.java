
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
//    1차원 배열을 활용한 arr
    static int[] arr;
    static int n;
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        backTrack(0);
        System.out.println(count);
    }
//    수평 좌우 대각 수직
    static void backTrack(int depth){
//        depth 가 n이면 각 행 마다 퀸을 놓을 수 있는 자리가 있다는 뜻
        if(depth == n){
            count++;
            return;
        }
        for(int i = 0; i< n; i++){
//            depth번째 행 i번째 열에 퀸을 놓음
            arr[depth] = i;
//                같은 열에 위치해있거나 대각선상에 위치하는지 확인
                if(isPossible(depth)) {
                    backTrack(depth + 1);
                }
            }
        }
    static boolean isPossible(int col){
        for(int j = 0; j< col; j++) {
//            첫번째 조건은 같은 열에 있으면
//            두번째 조건은 행이랑 열이 같으면? -> 
            if (arr[j] == arr[col] || Math.abs(col - j) == Math.abs(arr[col] - arr[j])) {
                return false;
            }
        }
        return true;
    }

}