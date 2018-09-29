item_price = [1050, 2200, 8575, 485, 234, 150, 399]
print("Price of the costliest item:",max(item_price))
print("Number of items in the retail store:",len(item_price))
print("Prices in Increasing order:",' '.join(sorted(item_price)))
print("Prices in Decreasing order:",' '.join(sorted(item_price,reverse=True)))
