'''
Question : Writing programming interview questions hasn't made me rich. Maybe trading Apple stocks will.
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Example : stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
'''

'''
Solution :

Brute Force :
    - max_profit = 0
    - go through every price (with its index as the time) --> i
        - go through later price  --> j
            - profit= price[i]-price[j]
            - max_profit = max(max_profit, profit)
Time : O(n^2)

Greedy : 
    - max_profit = price[0]- price[1]
    - At each iteration, our max_profit is either:
        - the same as the max_profit at the last time step, or
        - the max profit we can get by selling at the current_price. The max profit we can get by selling at the current_price  \ 
                is simply the difference between the current_price and the min_price from earlier in the day.   \
                If this difference is greater than the current max_profit, we have a new max_profit. 
                So for every price, well need to:
                - keep track of the lowest price we have seen so far
                - see if we can get a better profit
Time : O(n)
'''

def stockExchange(list_of_prices):
    '''
    :param list_of_prices: list like [5,1,19,12,9,51]
    :return: int maximum profit from buying and selling stocks like 50 for above list.
    '''
    if len(list_of_prices)<2:
        return IndexError('Atleast 2 prices should be given as input')
    max_profit = list_of_prices[1] - list_of_prices[0]
    minimum_value = list_of_prices[0] if list_of_prices[1]>=list_of_prices[0] else list_of_prices[1]
    for i in range(2,len(list_of_prices)):
        max_profit = max(max_profit, list_of_prices[i]-minimum_value)
        minimum_value = minimum_value if minimum_value <= list_of_prices[i] else list_of_prices[i]

    if max_profit < 0:
        return ValueError('All the sales are decreasing every day')
    elif max_profit == 0:
        return ValueError('All are same prices')
    else:
        return max_profit

print stockExchange([5,1,19,12,9,51])