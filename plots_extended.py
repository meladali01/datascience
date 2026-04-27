import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def save_fig(fig, path):
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def main():
    df = sns.load_dataset("tips")

    saved = []

    # 1) Distribution of tips
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot()
    sns.histplot(df['tip'], kde=True, ax=ax, color='skyblue')
    ax.set_title('Distribution of Tips')
    ax.set_xlabel('Tip ($)')
    save_fig(fig, 'dist_tip.png')
    saved.append('dist_tip.png')

    # 2) Scatter: total_bill vs tip with regression
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot()
    sns.regplot(x='total_bill', y='tip', data=df, scatter_kws={'alpha':0.6}, ax=ax)
    ax.set_title('Tip vs Total Bill')
    save_fig(fig, 'scatter_total_vs_tip.png')
    saved.append('scatter_total_vs_tip.png')

    # 3) Pairplot for small subset of variables
    pp = sns.pairplot(df[['total_bill','tip','size']])
    pp.fig.suptitle('Pairplot — total_bill, tip, size', y=1.02)
    pp.fig.savefig('pairplot.png')
    plt.close(pp.fig)
    saved.append('pairplot.png')

    # 4) Boxplot: tip by day
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot()
    sns.boxplot(x='day', y='tip', data=df, palette='Set2', ax=ax)
    ax.set_title('Tip by Day (boxplot)')
    save_fig(fig, 'box_tip_by_day.png')
    saved.append('box_tip_by_day.png')

    # 5) Violin plot: tip by time
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot()
    sns.violinplot(x='time', y='tip', data=df, inner='quartile', palette='Pastel1', ax=ax)
    ax.set_title('Tip by Time (violin)')
    save_fig(fig, 'violin_tip_by_time.png')
    saved.append('violin_tip_by_time.png')

    print('Saved plots:')
    for s in saved:
        print('-', s)


if __name__ == '__main__':
    main()
