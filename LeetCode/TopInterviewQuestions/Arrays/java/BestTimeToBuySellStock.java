package ICC.ICC.LeetCode.TopInterviewQuestions.Arrays;

public class BestTimeToBuySellStock {

    public static int maxProfit(int[] prices){
        int valley = Integer.MAX_VALUE;
        int peak = valley;
        int total = 0;
        
        for(int i = 0; i < prices.length; i++){
            if(prices[i] < peak){
                total += peak - valley;
                valley = prices[i];
                peak = valley;
            }else{
                peak = prices[i];
            }
        }
        total += peak - valley;
        return total;
    }

    public static void main(String[] args){
        int[] myArr = {7, 1, 5, 3, 6, 4};
        System.out.println(maxProfit(myArr));
    }
    
}
