def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # find difference between numbers. 2nd - 1st
        # if negative, discard.
        # if positive, keep track max profit.
        # update max_profit each time new number profit more than last
        max_profit = 0
        i = 0
        while i < len(prices)-1:
            for j in range (i+1,len(prices)):
                if prices[j]-prices[i]<0:
                    break
                else:
                    profit = prices[j]-prices[i]
                    if profit > max_profit:
                        max_profit = profit
            i+=1
        return max_profit

print(maxProfit([7,19,1,5,3,6,4]))