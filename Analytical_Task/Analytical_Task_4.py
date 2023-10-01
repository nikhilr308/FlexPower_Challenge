import pandas as pd

# Define the file path
file_path = r'C:\Users\Nikhil\Downloads\QuantChallenge-main\QuantChallenge-main\Applicants Data Task.xlsx'

# Read the first sheet (DE_Wind_PV_Prices)
data = pd.read_excel(file_path, sheet_name='DE_Wind_PV_Prices')

# Convert the 'hour' column to a datetime format
data['Datetime'] = pd.to_datetime(data['time'], format='%d-%m-%y %H:%M')

# Filter the data for the year 2021
data_2021 = data[data['Datetime'].dt.year == 2021]

# Combine the Wind and PV forecasts for each day
data_2021['Total Renewable Production (MW)'] = data_2021['Wind Day Ahead Forecast [in MW]'] + data_2021['PV Day Ahead Forecast [in MW]']

# Group the data by date and sum the total renewable production for each day in 2021
daily_total_renewable_production = data_2021.groupby(data_2021['Datetime'].dt.date)['Total Renewable Production (MW)'].sum()

# Find the day with the highest renewable energy production
highest_production_day = daily_total_renewable_production.idxmax()
highest_production_value = daily_total_renewable_production.max()

# Find the day with the lowest renewable energy production
lowest_production_day = daily_total_renewable_production.idxmin()
lowest_production_value = daily_total_renewable_production.min()

# Filter the data for the days with the highest and lowest production
highest_production_data = data_2021[data_2021['Datetime'].dt.date == highest_production_day]
lowest_production_data = data_2021[data_2021['Datetime'].dt.date == lowest_production_day]

# Calculate the average 'Day Ahead Price hourly [in EUR/MWh]' for the highest production day
average_price_highest_production = highest_production_data['Day Ahead Price hourly [in EUR/MWh]'].mean()

# Calculate the average 'Day Ahead Price hourly [in EUR/MWh]' for the lowest production day
average_price_lowest_production = lowest_production_data['Day Ahead Price hourly [in EUR/MWh]'].mean()

# Print the results
print(f"Day with the Highest Renewable Energy Production in 2021: {highest_production_day} with {highest_production_value:.2f} MW")
print(f"Average 'Day Ahead Price hourly [in EUR/MWh]' on the Highest Production Day: {average_price_highest_production:.2f} EUR/MWh")
print(f"Day with the Lowest Renewable Energy Production in 2021: {lowest_production_day} with {lowest_production_value:.2f} MW")
print(f"Average 'Day Ahead Price hourly [in EUR/MWh]' on the Lowest Production Day: {average_price_lowest_production:.2f} EUR/MWh")
