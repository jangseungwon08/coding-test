import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int [n];
        for(int i = 0; i< n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);
//        8 10 26 30으로 들어올릴 수 있는 최대 무게는? -> 무게가 고루 분포 되어야함
//        최적해를 뽑는 방법은 가장 작은 무게 * arr.length -> 모든 로프를 굳이 사용해야할 필요 x
//        그럼 안뽑는 경우는 무슨 경우지? -> 위 예 경우 26 30 을 뽑아서 26 * 2를 하면 52로 가장 많이 들 수 있음
        int weightSum = 0;
//        큰 무게부터 추가
        List<Integer> weightList = new ArrayList<>();
        for(int i = n-1; i >= 0; i--){
            weightList.add(arr[i]);
//            가장 작은 로프 * weightList > 현재까지의 들 수 있는 로프 무게
            if(weightList.get(weightList.size()-1) * weightList.size() > weightSum) weightSum = weightList.get(weightList.size()-1) * weightList.size();
        }
        System.out.println(weightSum);
    }
}