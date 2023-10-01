import pandas as pd

# Define the file path to your Excel file
file_path = r'C:\Users\Nikhil\Downloads\QuantChallenge-main\QuantChallenge-main\Applicants Data Task.xlsx'

# Read the first sheet (DE_Wind_PV_Prices)
data = pd.read_excel(file_path, sheet_name='DE_Wind_PV_Prices')

# Convert the 'hour' column to a datetime format
data['Datetime'] = pd.to_datetime(data['time'], format='%d-%m-%y %H:%M')

# Filter data for the year 2021
data_2021 = data[data['Datetime'].dt.year == 2021]

# Initialize variables for revenue and battery capacity
revenue = 0
battery_capacity = 1000  # 1 MWh in kWh

# Iterate through each day in 2021
for date, day_data in data_2021.groupby(data_2021['Datetime'].dt.date):
    # Calculate the total electricity consumed and produced during the day
    total_consumed = day_data['PV Day Ahead Forecast [in MW]'].sum() + day_data['Wind Day Ahead Forecast [in MW]'].sum()
    total_produced = day_data['Wind Intraday Forecast [in MW]'].sum() + day_data['PV Intraday Forecast [in MW]'].sum()
    
    # Calculate the net electricity available for charging or discharging
    net_electricity = total_produced - total_consumed
    
    # Check if the battery needs charging or discharging
    if net_electricity > 0:  # Charge the battery when excess electricity is available
        charge_amount = min(net_electricity, battery_capacity)  # Charge up to battery capacity
        battery_capacity -= charge_amount  # Reduce battery capacity
        revenue -= charge_amount * day_data['Intraday Price Price Quarter Hourly  [in EUR/MWh]'].mean() / 1000  # Charging cost
    elif net_electricity < 0:  # Discharge the battery when electricity demand is high
        discharge_amount = min(-net_electricity, battery_capacity)  # Discharge up to battery capacity
        battery_capacity += discharge_amount  # Increase battery capacity
        revenue += discharge_amount * day_data['Intraday Price Price Quarter Hourly  [in EUR/MWh]'].mean() / 1000  # Discharging revenue

# Print the total revenue for the year
print(f"Total revenue generated in 2021: {revenue:.2f} EUR")
