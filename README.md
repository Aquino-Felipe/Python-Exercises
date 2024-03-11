# Python-Exercises

The provided code is a simple program that tracks products entered by the user, calculates the total price, counts products over $1000, and identifies the cheapest product. Here's a breakdown of its functionality:

Initialization: The program starts by initializing several variables to zero or empty strings. These include total, subtotal, cheapest_price, count, and cheapest.
Infinite Loop: The program enters an infinite loop with while True:. This loop will continue indefinitely until a break statement is encountered.
Product Input: Inside the loop, the program prompts the user to input a product name and its price. The product name is converted to a string and stored in the variable product, while the price is converted to a float and stored in the variable price.
Count and Total Calculation: The count variable is incremented by 1 for each product entered, and the total variable is updated by adding the price of the current product.
Subtotal Calculation: If the price of the current product is greater than $1000, the subtotal variable is incremented by 1. This variable keeps track of the number of products that cost more than $1000.
Cheapest Product Identification: The program checks if the current product is cheaper than the previously identified cheapest product. If it is, the cheapest_price and cheapest variables are updated to reflect the new cheapest product.
Continuation Prompt: The user is then asked if they want to continue entering products. The input is validated to ensure it is either "Y" or "N". If "N" is entered, the loop breaks, and the program proceeds to the next step.
Output: After the loop ends, the program prints the total amount, the number of products over $1000, and the cheapest product's name and price. It also prints "END" centered within a line of 40 dashes.
This code demonstrates how to use loops, conditional statements, and user input to perform calculations and track information based on user input. It's a practical example of how to manage and process data in a simple, interactive Python program.

