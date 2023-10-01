import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = r'C:\Users\Nikhil\Downloads\QuantChallenge-main\QuantChallenge-main\Applicants Data Task.xlsx'

# Read the first sheet (DE_Wind_PV_Prices)
data = pd.read_excel(file_path, sheet_name='DE_Wind_PV_Prices')

data['Datetime'] = pd.to_datetime(data['time'], format='%d-%m-%y %H:%M')

# Filter data for the year 2021
data_2021 = data[data['Datetime'].dt.year == 2021]

# Calculate daily average production for Wind and PV for ID and DA separately
average_id_wind_production = data_2021.groupby(data_2021['Datetime'].dt.hour)['Wind Intraday Forecast [in MW]'].mean()
average_da_wind_production = data_2021.groupby(data_2021['Datetime'].dt.hour)['Wind Day Ahead Forecast [in MW]'].mean()
average_id_pv_production = data_2021.groupby(data_2021['Datetime'].dt.hour)['PV Intraday Forecast [in MW]'].mean()
average_da_pv_production = data_2021.groupby(data_2021['Datetime'].dt.hour)['PV Day Ahead Forecast [in MW]'].mean()

#print(average_id_pv_production)

# Create a 24-hour time range for the x-axis
hours = range(24)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(hours, average_id_wind_production, label='ID Wind Production', marker='o')
plt.plot(hours, average_da_wind_production, label='DA Wind Production', marker='o')
plt.plot(hours, average_id_pv_production, label='ID PV Production', marker='o')
plt.plot(hours, average_da_pv_production, label='DA PV Production', marker='o')

# Set labels and title
plt.xlabel('Hour of the Day')
plt.ylabel('Average Production (MW)')
plt.title('Average Wind and Solar Production in 2021 (ID and DA)')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()