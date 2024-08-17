package ICC.ICC.LeetCode.TopInterviewQuestions.Arrays;
/*
 * Solution to the leetcode problem 
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
 */
public class BestTimeBuySellStockI {
    public static int maxProfit(int[] prices) {
        if(prices.length == 0)
            return 0;

        int min_price = Integer.MAX_VALUE;
        int max_profit = 0;

        for(int i =0; i < prices.length; i++ ){
            if( prices[i] < min_price)
                min_price = prices[i];
            else if( max_profit < (prices[i]) - min_price )
                max_profit = prices[i] - min_price;
        }
        
        return max_profit;
    }

    public static void main(String args[]){
        int[] myArr = {7,1,5,3,6,4};
        System.out.println(maxProfit(myArr));
    }
    
}
