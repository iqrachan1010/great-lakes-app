import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ensure 'great_lakes.csv' is in the same directory as this script
df = pd.read_csv('great_lakes.csv')

# Metrics to compare
metrics = ['area', 'depth', 'vol', 'shoreline_ft', 'elevation_ft']

st.title("Great Lakes Comparison")

# Dropdown box for selecting a lake
lake = st.selectbox("Select a Lake", df['lake'].unique())

# Prepare data
data = df.set_index('lake')[metrics]

# Generate bar chart for each metric
for metric in metrics:
    fig, ax = plt.subplots()
    # Highlight the selected lake
    colors = ['orange' if idx == lake else 'skyblue' for idx in data.index]
    ax.bar(data.index, data[metric], color=colors)
    ax.set_title(f"{metric.title()} Comparison")
    ax.set_xlabel("Lake")
    ax.set_ylabel(metric.title())
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig, use_container_width=True)
