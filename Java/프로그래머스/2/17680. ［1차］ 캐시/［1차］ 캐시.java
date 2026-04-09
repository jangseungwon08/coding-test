import java.util.*;
class Solution {
    static int time;
    public int solution(int cacheSize, String[] cities) {
        lru(cacheSize, cities);
        return time;
    }
    static void lru(int cacheSize, String[] cities){
        time = 0;
        LinkedList<String> cache = new LinkedList<>();
        if(cacheSize == 0){
            time = cities.length * 5;
            return ;
        }
        for(String city: cities){
//             캐시 hit
            city = city.toLowerCase();
            if(cache.contains(city)){
                cache.remove(city);
                cache.addFirst(city);
                time += 1;
            }
//             DB 커넥트
            else{
//                cache에 없고 cache가 
                if(cache.size() < cacheSize){
                    cache.addFirst(city);
                    time += 5;
                }
                else{
                    cache.removeLast();
                    cache.addFirst(city);
                    time += 5;
                }
            }
        }
    }
}