stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 150
}

total_value = 0

while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock_name] * quantity
        total_value += investment

        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_value)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_value}")

print("Result saved in portfolio.txt")
