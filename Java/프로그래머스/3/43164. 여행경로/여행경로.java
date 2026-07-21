import java.util.*;

class Solution {
//     인접행렬
    static Map<String, List<String>> adjMap = new HashMap<>();
    static int totalTickets;
    static List<String> ans = new ArrayList<>();
    public List<String> solution(String[][] tickets) {
        String[] answer = {};
        totalTickets = tickets.length;
        for(int i = 0; i< tickets.length; i++){
            String from = tickets[i][0];
            String to = tickets[i][1];
//             Map에 해당 키가 없으면 
            if(!adjMap.containsKey(from)){
                adjMap.put(from, new ArrayList<>());
            }
            adjMap.get(from).add(to);
        }
        for(int i = 0; i< totalTickets; i++){
            List<String> toList = adjMap.get(tickets[i][0]);
            Collections.sort(toList);
        }
        ans.add("ICN");
        dfs("ICN", 0);
        return ans;
    }
    public static boolean dfs(String start, int usedCount){
//         종료조건 -> 사용한 티켓 개수가 총 티켓 개수랑 같으면
        if(usedCount == totalTickets){
            return true;
        }
//         해당 노드에서 출발하는 항공권이 없으면
        if(!adjMap.containsKey(start)) return false;
        
        List<String> nextTrip = adjMap.get(start);
//         for문 돌면서 다음 공항 끌어옴 
//         다음 공항 제거하고 answer에 추가 
        for(int i = 0; i< nextTrip.size(); i++){
            String next = nextTrip.get(i);
            nextTrip.remove(i);
            ans.add(next);
//             true를 못받았으면 
            if(dfs(next, usedCount+1)){
                return true;   
            }
//             이길이 아닌
            ans.remove(ans.size()-1);
            nextTrip.add(i, next);
        }
        return false;
    }
}