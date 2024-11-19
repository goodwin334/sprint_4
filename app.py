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

condition_order = ['salvage', 'fair', 'good', 'like new', 'excellent', 'new']

# Ensure the 'condition' column is a categorical type with the specified order
vehicles['condition'] = pd.Categorical(
    vehicles['condition'],
    categories=condition_order,
    ordered=True
)

# Sort the data by the 'condition' column
vehicles = vehicles.sort_values('condition')

# Create a histogram grouping vehicles by condition with price on the y-axis
fig6 = plt.histogram(
    vehicles,
    x='condition',
    y='price',
    histfunc='avg',  # Aggregate by average price
    title='Average Price of Vehicles by Condition (Sorted)',
    labels={'condition': 'Vehicle Condition', 'price': 'Average Price'},
    color='condition',  # Optional: Color bars by condition
    width=800,
    height=600
)

st.plotly_chart(fig6)