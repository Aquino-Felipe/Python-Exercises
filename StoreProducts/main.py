# Initialize variables to track total price, count of products, cheapest product price, and cheapest product name
total = subtotal = cheapest_price = count = 0
cheapest = " "

# Start an infinite loop to continuously prompt for product details
while True:
    # Prompt for product name and convert to string
    product = str(input("Type a product: "))
    # Prompt for product price and convert to float
    price = float(input("Price: $"))
    # Increment the count of products entered
    count += 1
    # Add the price of the current product to the total
    total += price
    
    # Check if the price is greater than $1000 and increment subtotal if true
    if price > 1000:
        subtotal += 1
  
    # For the first product, set it as the cheapest
    if count == 1:
        cheapest_price = price
        cheapest = product
    else:
        # If the current product is cheaper than the previously cheapest, update cheapest variables
        if price < cheapest_price:
            cheapest_price = price
            cheapest = product
      
    # Initialize condition variable for user input
    cond = " "
    # Validate user's response to continue, ensuring it's either "Y" or "N"
    while cond not in "YN":
        cond = str(input("Would you like to continue? [Y/N]: ")).strip().upper()[0]
    # If user inputs "N", break the loop
    if cond == "N":
        break

# Print the total amount, number of products over $1000, and the cheapest product's name and price
print(f"The total amount is {total}")
print(f"We have {subtotal} products above $1000.00")
print(f"The cheapest product is {cheapest} for {cheapest_price}")
# Print "END" centered within a line of 40 dashes
print("{:-^40}".format("END"))
