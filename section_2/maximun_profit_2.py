N = int(input())

purchase_price = int(input())
profit = -2000000000
for _ in range(N-1):
    price = int(input())
    profit = max(profit, (price-purchase_price))
    purchase_price = min(price, purchase_price)

print(profit)