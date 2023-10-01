import pandas as pd
import matplotlib.pyplot as plt

# Define the file path to your Excel file
file_path = r'C:\Users\Nikhil\Downloads\QuantChallenge-main\QuantChallenge-main\Applicants Data Task.xlsx'

# Read the first sheet (DE_Wind_PV_Prices)
data = pd.read_excel(file_path, sheet_name='DE_Wind_PV_Prices')

# Assuming 'Datetime' is already in datetime format
# Filter the data for the time range between 13:00 and 14:00 for all months
# Convert the 'hour' column to a datetime format
data['Datetime'] = pd.to_datetime(data['time'], format='%d-%m-%y %H:%M')

# Define input parameters
time_range = ('13:00', '14:00')
filtered_data = data[
  (data['Datetime'].dt.strftime('%H:%M') >= time_range[0]) &
  (data['Datetime'].dt.strftime('%H:%M') <= time_range[1])
]

# Define your trading conditions
buy_condition = (filtered_data['Day Ahead Price hourly [in EUR/MWh]'] < filtered_data['Intraday Price Hourly  [in EUR/MWh]'])
sell_condition = (filtered_data['Day Ahead Price hourly [in EUR/MWh]'] > filtered_data['Intraday Price Hourly  [in EUR/MWh]'])

# Initialize capital and position
capital = 0
position = 0

# Initialize a list to track cumulative performance
cumulative_performance = []

# Initialize a list to track trading decisions
trading_decisions = []

# Iterate through the filtered data
for index, row in filtered_data.iterrows():
    # Make a trading decision
    if buy_condition.any():
        # Go long (buy)
        position += 100

        # Calculate the capital used to buy the position
        capital_used = 100 * row['Intraday Price Hourly  [in EUR/MWh]']

        # Subtract the capital used from the total capital
        capital -= capital_used

        # Add the trading decision to the list
        trading_decisions.append("Buy")
    elif sell_condition.any():
        # Go short (sell)
        position -= 100

        # Calculate the capital generated from selling the position
        capital_generated = 100 * row['Intraday Price Hourly  [in EUR/MWh]']

        # Add the capital generated to the total capital
        capital += capital_generated

        # Add the trading decision to the list
        trading_decisions.append("Sell")
    else:
        # Hold
        trading_decisions.append("Hold")

    # Calculate the cumulative performance
    cumulative_performance.append(capital)

# Print the trading decisions
print(len(trading_decisions))
