import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load preprocessed data
df = pd.read_csv('vehicles_us.csv')

st.title('Vehicle Data Analysis')

# Show dataset
st.write("Here’s a preview of the dataset:")
st.write(df.head())

# Scatter plot
st.write("Price vs Odometer")
fig, ax = plt.subplots()
ax.scatter(df['odometer'], df['price'], alpha=0.5)
ax.set_xlabel('Odometer')
ax.set_ylabel('Price')
st.pyplot(fig)

# Load the preprocessed dataset (replace 'vehicles_us.csv' with your dataset file)
df = pd.read_csv('vehicles_us.csv')

# App title
st.title('Vehicle Data Analysis and Visualizations')

# Show dataset preview
st.write("### Dataset Preview")
st.write(df.head())

# Sidebar for user options
st.sidebar.header('Select Visualization')

# User selects the feature for histogram
option = st.sidebar.selectbox(
    'Select the feature for histogram',
    ('price', 'model_year')
)

# Create a histogram for the selected feature
st.write(f"### Histogram of {option.capitalize()}")

# Plot the histogram
fig, ax = plt.subplots()
ax.hist(df[option].dropna(), bins=20, color='lightgreen', edgecolor='black')
ax.set_xlabel(option.capitalize())
ax.set_ylabel('Number of Vehicles')
ax.set_title(f'Distribution of {option.capitalize()}')
st.pyplot(fig)

