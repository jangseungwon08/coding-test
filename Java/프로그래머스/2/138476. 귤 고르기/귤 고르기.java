import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
Map<Integer, Integer> tangerineMap = new HashMap<>();
        for (int i = 0; i < tangerine.length; i++) {
            if(tangerineMap.containsKey(tangerine[i])){
                tangerineMap.put(tangerine[i], tangerineMap.get(tangerine[i]) + 1);
            }
            else{
                tangerineMap.put(tangerine[i], 1);
            }
        }
        List<Integer> keySet = new ArrayList<>(tangerineMap.keySet());
        keySet.sort((o1, o2) -> tangerineMap.get(o2).compareTo(tangerineMap.get(o1)));
        for(Integer key: keySet){
            if(k > 0) {
                answer++;
                k -= tangerineMap.get(key);
            }
            else break;
        }
        return answer;
    }
}