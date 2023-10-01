import pandas as pd

# Define the file path
file_path = r'C:\Users\Nikhil\Downloads\QuantChallenge-main\QuantChallenge-main\Applicants Data Task.xlsx'

# Read the first sheet (DE_Wind_PV_Prices)
data = pd.read_excel(file_path, sheet_name='DE_Wind_PV_Prices')

# Convert the 'hour' column to a datetime format
data['Datetime'] = pd.to_datetime(data['time'], format='%d-%m-%y %H:%M')

# Extract the year from the 'Datetime' column
data['Year'] = data['Datetime'].dt.year

# Filter data for the year 2021
data_2021 = data[data['Year'] == 2021]

# Calculate the total Wind and PV Power for 2021 (in MWh) on Day Ahead (DA)
total_da_wind_forecast_mwh = data_2021['Wind Day Ahead Forecast [in MW]'].sum() / 4  # Divide by 4 for hourly values
total_da_pv_forecast_mwh = data_2021['PV Day Ahead Forecast [in MW]'].sum() / 4  # Divide by 4 for hourly values

# Calculate the total Wind and PV Power for 2021 (in MWh) on Intraday (ID)
total_id_wind_forecast_mwh = data_2021['Wind Intraday Forecast [in MW]'].sum() / 4  # Divide by 4 for hourly values
total_id_pv_forecast_mwh = data_2021['PV Intraday Forecast [in MW]'].sum() / 4  # Divide by 4 for hourly values

print(f"Total Wind Power forecasted on Day Ahead (DA) in 2021: {total_da_wind_forecast_mwh:.2f} MWh")
print(f"Total PV Power forecasted on Day Ahead (DA) in 2021: {total_da_pv_forecast_mwh:.2f} MWh")
print(f"Total Wind Power forecasted on Intraday (ID) in 2021: {total_id_wind_forecast_mwh:.2f} MWh")
print(f"Total PV Power forecasted on Intraday (ID) in 2021: {total_id_pv_forecast_mwh:.2f} MWh")
