import pandas as pd
import matplotlib.pyplot as plt

# Define the file path
file_path = r'C:\Users\Nikhil\Downloads\QuantChallenge-main\QuantChallenge-main\Applicants Data Task.xlsx'

# Read the first sheet (DE_Wind_PV_Prices)
data = pd.read_excel(file_path, sheet_name='DE_Wind_PV_Prices')

data['Datetime'] = pd.to_datetime(data['time'], format='%d-%m-%y %H:%M')

data_2021 = data[data['Datetime'].dt.year == 2021]



# hour_da_wind_forecast = data.groupby(data['Datetime'].dt.hour)['Wind Day Ahead Forecast [in MW]'].sum()

# hour_da_pv_forecast = data.groupby(data['Datetime'].dt.hour)['PV Day Ahead Forecast [in MW]'].sum()

average_da_price = data_2021['Day Ahead Price hourly [in EUR/MWh]'].mean()
print(average_da_price)

average_id_price = data_2021['Intraday Price Hourly  [in EUR/MWh]'].mean()
print(average_id_price)

da_price_wind_pv_sum = data.groupby(data['Datetime'].dt.date)['Day Ahead Price hourly [in EUR/MWh]'].sum()

#print(da_price_wind_pv_sum)

# Sum the hourly average values of wind and divide by the number of hours in the quarter.
average_value_of_wind_pv_1 = da_price_wind_pv_sum.mean() 

print(f"Average Day Ahead (DA) hourly price in 2021: {average_da_price:.2f} EUR/MWh")
print(f"Average Intraday hourly price in 2021: {average_id_price:.2f} EUR/MWh")


# Print the average value of wind for the quarter in EUR/MWh
#print(average_value_of_wind_pv_1)


