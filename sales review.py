# Define the product names, prices, and last week's sales
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price average
total_price = sum(prices)
average_price = total_price / len(prices)
print("Total price average:", average_price)

# Create a new price list with $5 reduction
new_prices = [price - 5 for price in prices]
print("New price list:", new_prices)

# Calculate the total revenue generated
total_revenue = sum(price * sales for price, sales in zip(prices, last_week))
print("Total revenue:", total_revenue)

# Calculate the average daily revenue
average_daily_revenue = total_revenue / 7
print("Average daily revenue:", average_daily_revenue)

# Find products less than $30 in the new price list
products_under_30 = [product for product, price in zip(products, new_prices) if price < 30]
print("Products less than $30:", products_under_30)
