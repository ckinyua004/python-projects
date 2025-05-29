import matplotlib.pyplot as plt

# Simulated data based on estimates for Kenya's income distribution
income_groups = [
    "Bottom 10%", "Next 10%", "Next 10%", "Next 10%", "Next 10%",
    "Next 10%", "Next 10%", "Next 10%", "Next 10%", "Top 10%"
]
# Approximate income share percentages for each decile
income_shares = [
    1, 2, 3, 4, 5,
    6, 8, 10, 15, 46  # Top 10% share increased to approx. 46%
]

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(income_groups, income_shares, color='skyblue')
plt.title("Estimated Income Distribution in Kenya by Population Deciles")
plt.xlabel("Income Groups")
plt.ylabel("Share of National Income (%)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Highlight the top 10% bar
bars[-1].set_color('darkblue')
bars[-1].set_label('Top 10%')

plt.legend()
plt.tight_layout()
plt.show()
