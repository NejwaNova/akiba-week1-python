exchange_rate = 150

usd = float(input("Enter amount in USD: "))

etb = usd * exchange_rate

print("\n==============================")
print("      CURRENCY EXCHANGE")
print("==============================")

print(f"\nUSD Amount: {usd:,.0f}")

print(f"\nExchange Rate: 1 USD = {exchange_rate} ETB")

print(f"\nETB Amount: {etb:,.0f} ETB")

print("==============================")