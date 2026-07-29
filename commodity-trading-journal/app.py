import yfinance as yf
import matplotlib.pyplot as plt


brent=yf.download('BZ=F',start='2026-01-01')

#PLot
plt.figure(figsize=(12,6))
plt.plot(brent['Close'])
plt.axvline('2026-07-29', color='red', linestyle='--', label='Iran attack - long entry')
plt.title('Brent Crude Oil Price — 2026')
plt.legend()
plt.savefig('brent_trade_entry.png')
plt.show()