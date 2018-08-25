N = int(input())
price_list = [int(input()) for _ in range(N)]

purchase_price = price_list[0]
profit = price_list[1] - purchase_price
for price in price_list[1:]:
    profit = max(profit, (price-purchase_price))
    purchase_price = min(price, purchase_price)

print(profit)