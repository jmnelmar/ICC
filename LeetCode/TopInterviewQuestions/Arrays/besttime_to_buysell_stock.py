'''
Best Time To Buy Sell Stock leetcode challengue
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Algorithm 
 original iteration 
 m
 r 
[7, 1, 5, 3, 6, 4]  l = 0, r = 0, m = 0
 l

 iteration 1
 m
    r 
[7, 1, 5, 3, 6, 4]  l = 0, r = 1, mim = 1 max
 l

 iteration n - 1
    m
                r 
[7, 1, 5, 3, 6, 4]  l = 0, r = 1, mim = 1, max = ,bought = 1
    l


'''
import sys

def maxProfit(prices) -> int:
    valley = sys.maxsize
    peak = valley
    total = 0

    for i in range(len(prices)):
        if prices[i] < peak:
            total += peak - valley
            valley = prices[i]
            peak = valley
        else:
            peak = prices[i]
    total += peak - valley
    return total

arr = [7, 1, 5, 3, 6, 4]

print(maxProfit(arr))