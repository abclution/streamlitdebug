#hi
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['col1', 'col2', 'col3'])

st.line_chart(
    chart_data,
    x = 'col1',
    y = ['col2', 'col3'],
    color = ['#FF0000', '#0000FF']  # Optional
)

energyUsageYearlyKwH_BTC = 2354234523456
energyUsageYearlyKwH_BCH = 237645675673543
# Define the range of values
start_value = 0.007
end_value = 0.35
step = 0.001

# Define the variable for energy usage
#energyUsageYearlyKwH = 1000  # Example value, replace with your actual value

# Create a list of values for column 1
costPerKwH = [round(start_value + i * step, 3) for i in range(int((end_value - start_value) / step) + 1)]

# Create a dictionary to hold the data
data = {
    "Electricity Cost (per KwH)": costPerKwH,
    "Yearly, BTC Security Budget": [value * energyUsageYearlyKwH_BTC for value in costPerKwH],
    "Yearly, BCH Security Budget": [value * energyUsageYearlyKwH_BCH for value in costPerKwH]
}

df = pd.DataFrame(data)

st.line_chart(
    df,
    x='Electricity Cost (per KwH)',
    y=['Yearly, BTC Security Budget','Yearly, BCH Security Budget'],
    color=['#F2A900', '#0AC18E']
    )
