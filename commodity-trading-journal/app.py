import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import os

# Download Brent crude price data
brent = yf.download('BZ=F', start='2026-01-01')

# Your exact entry details
entry_date = pd.Timestamp('2026-07-29')
entry_price = 88.14  # Your actual entry price — update this to exact figure

# Save path
save_path = os.path.expanduser('~/Desktop/Commodity projects/commodity-trading-journal/brent_trade_entry.png')

# Plot
plt.figure(figsize=(12,6))
plt.plot(brent.index, brent['Close'], color='blue', linewidth=1.5, label='Brent Crude Price')

# Vertical line at entry date
plt.axvline(entry_date, color='red', linestyle='--', label=f'Long Entry — Iran attack')

# Horizontal line at entry price
plt.axhline(entry_price, color='green', linestyle=':', label=f'Entry Price: ${entry_price}')

# Stop loss line
plt.axhline(85.00, color='orange', linestyle=':', label='Stop Loss: $85.00')

plt.title('Brent Crude Oil — Long Position (29 July 2026)\nMiddle East Escalation Trade')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.tight_layout()
plt.savefig(save_path)
plt.show()

print(f"Chart saved to: {save_path}")
