import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(5)
dates = pd.date_range(start="2025-11-01", periods=30, freq='D')
base = np.linspace(20, 25, 30)
noise = np.random.normal(0, 0.8, 30)
series = base + noise

spike_indices = [5, 12, 20]
series[spike_indices] += [5, -4, 6]

df = pd.DataFrame({"date": dates, "temp": series})

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['date'], df['temp'], marker='o', label='Nhiệt độ')
z = np.polyfit(np.arange(len(df)), df['temp'], 1)
trend = np.polyval(z, np.arange(len(df)))
ax.plot(df['date'], trend, color='red', linestyle='--', label='Trendline')
for i in spike_indices:
    ax.axvline(df['date'].iloc[i], color='orange', linestyle=':', alpha=0.8)
    ax.annotate(f"Spike ({df['temp'].iloc[i]:.1f})", xy=(df['date'].iloc[i], df['temp'].iloc[i]),
                xytext=(df['date'].iloc[i], df['temp'].iloc[i]+2),
                arrowprops=dict(arrowstyle='->'), fontsize=9)

special = df['date'].iloc[10]
ax.axvline(special, color='purple', alpha=0.6)
ax.text(special, ax.get_ylim()[1]-0.5, "Mốc đặc biệt",
        rotation=90, va='top', color='purple')

ax.set_title("Bài 9: Chuỗi thời gian nhiệt độ trong tháng")
ax.set_xlabel("Ngày")
ax.set_ylabel("Nhiệt độ (°C)")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
