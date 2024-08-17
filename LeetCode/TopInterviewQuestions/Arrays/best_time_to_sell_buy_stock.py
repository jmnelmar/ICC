def maxProfit( prices:list) -> int:
    max_profit = 0
    profit = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
    
    return max_profit

#Eficient solution.
def maxProfit_(prices:list) -> int:
    max_stock,min_stock,max_profit, profit = 0,0,0,0

    for i in range(len(prices)):
        max_stock = max( prices[1:] )
        if max_stock > prices[i]:
            
    

prices = [7,1,5,3,6,4]
print(prices[1:])
#print(maxProfit(prices))
    
