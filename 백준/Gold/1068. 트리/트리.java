import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static List<List<Integer>> tree;
    static boolean[] isVisited;
    static int n;
    static int root;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        isVisited = new boolean[n];
        tree = new ArrayList<>();
        int count = 0;
        for (int i = 0; i < n; i++) {
            tree.add(new ArrayList<>());
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i< n; i++){
            int node = Integer.parseInt(st.nextToken());
            if(node == -1){
                root = i;
                continue;
            }
            tree.get(node).add(i);
        }
        int deleteNode = Integer.parseInt(br.readLine());
//        루트노드가 삭제되었으면 리프노드 없으니까
        if(deleteNode == root){
            System.out.println(count);
            return;
        }
        for(int i = 0; i< n; i++){
//            부모노드가 deleteNode를 갖고 있으면
            if(i == deleteNode) continue;

            if(tree.get(i).contains(deleteNode)){
                tree.get(i).remove(Integer.valueOf(deleteNode));
                break;
            }
        }
        isVisited[deleteNode] = true;
        dfs(deleteNode);
        for(int i = 0; i< n; i++){
//            삭제되지 않았고 리프노드이면
            if(!isVisited[i] && tree.get(i).isEmpty()){
                count++;
            }
        }
        System.out.println(count);
    }
    static void dfs(int deleteNode){
//        리프 노드이면 return
        if(tree.get(deleteNode).isEmpty()){
            return;
        }
        //        deleteNode로 된 배열은 모두 visited처리
        for(int i = 0; i< tree.get(deleteNode).size(); i++){
//            삭제되는 노드인데 방문하지 않았다면
            if(!isVisited[tree.get(deleteNode).get(i)]){
//                방문처리
                isVisited[tree.get(deleteNode).get(i)] = true;
                dfs(tree.get(deleteNode).get(i));
            }
        }
    }

}
