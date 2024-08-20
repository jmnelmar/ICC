def maxProfit( prices:list) -> int:
    max_profit = 0
    profit = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
    
    return max_profit

#Eficient solution o(n).
def maxProfit_(prices:list) -> int:
    min_price, max_profit = float("inf"), 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        max_profit = max(max_profit, (prices[i] - min_price))

    return max_profit    

    

prices = [7,1,5,3,6,4]
#print(prices[1:])
print(maxProfit_(prices))
    
