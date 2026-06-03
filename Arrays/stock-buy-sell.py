def stock_buy_sell(prices):
    min_price = float('inf')
    max_profit = 0

    for i in prices:
        if i < min_price:
            min_price = i
        else:
            max_profit = max(max_profit, i - min_price)
    return max_profit

prices = list(map(int, input().split()))
print(stock_buy_sell(prices))