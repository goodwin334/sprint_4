import pandas as pd
import streamlit as st
import plotly.express as plt
import altair as aa
vehicles = pd.read_csv('vehicles_us.csv')
columns_to_convert = ['model_year', 'cylinders', 'is_4wd', 'odometer']
for column in columns_to_convert:
    vehicles[column] = vehicles[column].fillna(0).astype(int)
vehicles['model_year'] = vehicles['model_year'].fillna('0000')
vehicles['cylinders'] = vehicles['cylinders'].fillna('00')
vehicles['odometer'] = vehicles['odometer'].replace(0, 'blank')
vehicles['paint_color'] = vehicles['paint_color'].replace(0, 'blank')


st.header("Exploratory Data Analysis")
vehicles['brand'] = vehicles['model'].str.split(' ').str[0]

# Add a header
st.header("Scatterplot with Brand Filter")

# Checkbox to enable filtering
filter_enabled = st.checkbox("Filter by Brand")

# Dropdown to select a brand (only visible if the checkbox is enabled)
if filter_enabled:
    selected_brand = st.selectbox(
        "Select a Brand",
        options=vehicles['brand'].unique(),
        index=0  # Default to the first option
    )
    # Filter the data by the selected brand
    filtered_data = vehicles[vehicles['brand'] == selected_brand]
else:
    # If the checkbox is not enabled, show all data
    filtered_data = vehicles

# Scatterplot
fig = plt.scatter(
    filtered_data,
    x='odometer',
    y='price',
    color='brand',
    title="Scatterplot of Odometer vs Price",
    labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)', 'brand': 'Brand'},
    width=800,
    height=600
)

# Show the scatterplot in Streamlit
st.plotly_chart(fig)

fig3 = plt.scatter(
    vehicles,
    x='days_listed',
    y='odometer',
    title='Scatterplot of Days Posted vs Odometer Reading',
    labels={'days_listed': 'Days Listed', 'odometer': 'Odometer (miles)'},
    width=800,
    height=600
)
st.plotly_chart(fig3)