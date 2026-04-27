import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    # Load example dataset from seaborn
    df = sns.load_dataset("tips")

    # Compute average tip by day
    avg = df.groupby("day")["tip"].mean().reset_index()

    # Create bar plot
    plt.figure(figsize=(7,5))
    sns.barplot(x="day", y="tip", data=avg, palette="Blues_d")
    plt.title("Average Tip by Day")
    plt.ylabel("Average tip ($)")
    plt.xlabel("Day of week")
    plt.tight_layout()

    # Save and show
    out = "avg_tip_by_day.png"
    plt.savefig(out)
    print(f"Saved plot to {out}")
    plt.show()


if __name__ == "__main__":
    main()
