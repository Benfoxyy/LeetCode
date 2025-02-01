prices = [2,4,1]

buy =  prices.index(min(prices))

if prices[buy+1:] > prices[buy:]:
    print(max(prices[buy+1:]) - prices[buy])
else:
    print(0)