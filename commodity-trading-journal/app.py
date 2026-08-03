import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import os

brent = yf.download('BZ=F', start='2026-01-01')

entry_date = pd.Timestamp('2026-07-29')
entry_price = 88.14
stop_loss = 82.00

brent_from_entry = brent[brent.index >= entry_date].copy()
brent_from_entry['pnl_pct'] = (brent_from_entry['Close'] - entry_price) / entry_price * 100

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

ax1.plot(brent.index, brent['Close'], color='blue', linewidth=1.5)
ax1.axvline(entry_date, color='red', linestyle='--', label='Long Entry — Iran attack')
ax1.axhline(entry_price, color='green', linestyle=':', label=f'Entry: ${entry_price}')
ax1.axhline(stop_loss, color='red', linestyle=':', label=f'Stop Loss: ${stop_loss}')
ax1.set_title('Brent Crude — Long CFD Position (29 July 2026)')
ax1.set_ylabel('Price (USD)')
ax1.legend()

ax2.plot(brent_from_entry.index, brent_from_entry['pnl_pct'], color='purple')
ax2.axhline(0, color='grey', linestyle='-', linewidth=0.5)
ax2.fill_between(brent_from_entry.index, brent_from_entry['pnl_pct'], 0,
                 where=brent_from_entry['pnl_pct'] >= 0, alpha=0.3, color='green')
ax2.fill_between(brent_from_entry.index, brent_from_entry['pnl_pct'], 0,
                 where=brent_from_entry['pnl_pct'] < 0, alpha=0.3, color='red')
ax2.set_ylabel('P&L from Entry (%)')
ax2.set_xlabel('Date')

save_path = os.path.expanduser('~/Desktop/Commodity projects/commodity-trading-journal/brent_trade_entry.png')
plt.tight_layout()
plt.savefig(save_path)
plt.show()
print(f"Chart saved to: {save_path}")