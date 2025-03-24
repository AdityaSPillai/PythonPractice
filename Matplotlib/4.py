import matplotlib.pyplot as plt

companies = ["Company A", "Company B", "Company C", "Company D", "Company E"]
market_shares = [30, 20, 25, 15, 10]

colors = ["lightblue", "darkgreen", "yellow", "orange", "purple"]

plt.figure(figsize=(7, 7))
plt.pie(market_shares, labels=companies, colors=colors, autopct="%1.1f%%", startangle=140)

plt.legend(title="Companies", loc="best")

plt.title("Market Share Distribution")

plt.show()