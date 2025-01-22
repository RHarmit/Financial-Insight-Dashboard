import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create dummy data
np.random.seed(42)
data = {
    "Quarter": ["Q1 2023", "Q2 2023", "Q3 2023", "Q4 2023", "Q1 2024"],
    "Revenue": np.random.uniform(100, 200, 5).round(2),
    "Cost": np.random.uniform(50, 100, 5).round(2),
    "Active_Users": np.random.randint(50000, 100000, 5),
    "Transactions": np.random.randint(100000, 200000, 5),
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate additional metrics
df["Profit"] = (df["Revenue"] - df["Cost"]).round(2)
df["ARPU"] = (df["Revenue"] / df["Active_Users"] * 1000).round(2)  # Average Revenue Per User

# Generate summary statistics
summary_stats = df.describe()

def plot_metrics(df):
    # Plot Revenue, Cost, and Profit
    plt.figure(figsize=(10, 6))
    plt.plot(df["Quarter"], df["Revenue"], label="Revenue", marker="o")
    plt.plot(df["Quarter"], df["Cost"], label="Cost", marker="o")
    plt.plot(df["Quarter"], df["Profit"], label="Profit", marker="o")
    plt.title("Revenue, Cost, and Profit Over Quarters")
    plt.xlabel("Quarter")
    plt.ylabel("Amount (in $)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot Active Users and Transactions
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel("Quarter")
    ax1.set_ylabel("Active Users", color="tab:blue")
    ax1.plot(df["Quarter"], df["Active_Users"], label="Active Users", marker="o", color="tab:blue")
    ax1.tick_params(axis='y', labelcolor="tab:blue")

    ax2 = ax1.twinx()
    ax2.set_ylabel("Transactions", color="tab:orange")
    ax2.plot(df["Quarter"], df["Transactions"], label="Transactions", marker="o", color="tab:orange")
    ax2.tick_params(axis='y', labelcolor="tab:orange")

    plt.title("Active Users and Transactions Over Quarters")
    fig.tight_layout()
    plt.show()

    # Plot ARPU (Average Revenue Per User)
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Quarter", y="ARPU", data=df, palette="viridis")
    plt.title("Average Revenue Per User (ARPU) Over Quarters")
    plt.xlabel("Quarter")
    plt.ylabel("ARPU ($)")
    plt.show()

# Display the data
print("Dummy Data:\n")
print(df)

# Display summary statistics
print("\nSummary Statistics:\n")
print(summary_stats)

# Plot metrics
plot_metrics(df)
