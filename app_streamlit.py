import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    return sns.load_dataset('tips')


def plot_distribution(df):
    fig, ax = plt.subplots(figsize=(7,4))
    sns.histplot(df['tip'], kde=True, ax=ax, color='skyblue')
    ax.set_title('Distribution of Tips')
    return fig


def plot_scatter(df):
    fig, ax = plt.subplots(figsize=(7,4))
    sns.regplot(x='total_bill', y='tip', data=df, scatter_kws={'alpha':0.6}, ax=ax)
    ax.set_title('Tip vs Total Bill')
    return fig


def plot_box(df):
    fig, ax = plt.subplots(figsize=(7,4))
    sns.boxplot(x='day', y='tip', data=df, palette='Set2', ax=ax)
    ax.set_title('Tip by Day (boxplot)')
    return fig


def plot_pair(df):
    pp = sns.pairplot(df[['total_bill','tip','size']])
    return pp.fig


def main():
    st.title('Tips dataset explorer')
    df = load_data()

    st.sidebar.header('Controls')
    plot_type = st.sidebar.selectbox('Plot type', ['Table','Distribution','Scatter','Boxplot','Pairplot'])

    if plot_type == 'Table':
        st.dataframe(df)
    elif plot_type == 'Distribution':
        st.pyplot(plot_distribution(df))
    elif plot_type == 'Scatter':
        st.pyplot(plot_scatter(df))
    elif plot_type == 'Boxplot':
        st.pyplot(plot_box(df))
    elif plot_type == 'Pairplot':
        st.pyplot(plot_pair(df))

    st.sidebar.markdown('Use the plot selector to choose a visualization.')

if __name__ == '__main__':
    main()
