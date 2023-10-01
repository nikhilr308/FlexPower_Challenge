import pandas as pd

# Define the file path
file_path = r'C:\Users\Nikhil\Downloads\QuantChallenge-main\QuantChallenge-main\Applicants Data Task.xlsx'

# Read the first sheet (DE_Wind_PV_Prices)
data = pd.read_excel(file_path, sheet_name='DE_Wind_PV_Prices')

# Convert the 'hour' column to a datetime format
data['Datetime'] = pd.to_datetime(data['time'], format='%d-%m-%y %H:%M')

# Create a new column 'Day Type' to identify weekdays and weekends
data['Day Type'] = data['Datetime'].dt.dayofweek  # Monday=0, Sunday=6
data['Day Type'] = data['Day Type'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

# Group the data by 'Day Type' and calculate the average DA price
average_da_price_by_daytype = data.groupby('Day Type')['Day Ahead Price hourly [in EUR/MWh]'].mean()

# Print the results
print("Average Hourly DA Price on Weekdays:")
print(average_da_price_by_daytype['Weekday'])

print("Average Hourly DA Price on Weekends:")
print(average_da_price_by_daytype['Weekend'])
