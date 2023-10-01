
import sqlite3
import csv
from flask import Flask
from flask_restful import Api, Resource, reqparse
from datetime import datetime



# Connect to the SQLite database
connection = sqlite3.connect('trades.sqlite')

# Create a cursor object
cursor = connection.cursor()

# Execute an SQL query to retrieve data from the table
cursor.execute('SELECT * FROM "epex_12_20_12_13" ')

# Fetch all rows
rows = cursor.fetchall()

# Specify the output CSV file name
csv_file_name = 'trades.csv'

# Write the data to a CSV file
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])  # Write column headers
    csv_writer.writerows(rows)

# Close the cursor and connection
cursor.close()
connection.close()

# Specify the CSV file name
csv_file_name = 'trades.csv'

#assignment 1
# Define functions to compute total buy and sell volumes as per the assignment 1
def compute_total_buy_volume(csv_file, strategy_name):
    total_buy_volume = 0
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['side'] == 'buy' and row['strategy'] == strategy_name:
                total_buy_volume += int(row['quantity'])
    return total_buy_volume

def compute_total_sell_volume(csv_file, strategy_name):
    total_sell_volume = 0
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['side'] == 'sell' and row['strategy'] == strategy_name:
                total_sell_volume += int(row['quantity'])
    return total_sell_volume

# Specify the strategy name for "flex power"
strategy_name_flex_power = "strategy_1"

# Calculate and print the total buy and sell volumes for "flex power" from the CSV file
total_buy_volume = compute_total_buy_volume(csv_file_name, strategy_name_flex_power)
total_sell_volume = compute_total_sell_volume(csv_file_name, strategy_name_flex_power)

print(f"Total Buy Volume for {strategy_name_flex_power}: {total_buy_volume}")
print(f"Total Sell Volume for {strategy_name_flex_power}: {total_sell_volume}")

# Specify the strategy name for "flex power"
strategy_name_flex_power = "strategy_2"

# Calculate and print the total buy and sell volumes for "flex power" from the CSV file
total_buy_volume = compute_total_buy_volume(csv_file_name, strategy_name_flex_power)
total_sell_volume = compute_total_sell_volume(csv_file_name, strategy_name_flex_power)

print(f"Total Buy Volume for {strategy_name_flex_power}: {total_buy_volume}")
print(f"Total Sell Volume for {strategy_name_flex_power}: {total_sell_volume}")



# Define functions to compute total buy and sell volumes for all stratergies
def compute_total_buy_volume_combined_stratergies(csv_file):
    total_buy_volume = 0
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['side'] == 'buy':
                total_buy_volume += int(row['quantity'])
    return total_buy_volume

def compute_total_sell_volume_combined_stratergies(csv_file):
    total_sell_volume = 0
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['side'] == 'sell' :
                total_sell_volume += int(row['quantity'])
    return total_sell_volume

# Calculate and print the total buy and sell volumes for "flex power" from the CSV file
total_buy_volume_1= compute_total_buy_volume_combined_stratergies(csv_file_name)
total_sell_volume_1 = compute_total_sell_volume_combined_stratergies(csv_file_name)

print(f"Total Buy Volume for combined stratergies: {total_buy_volume_1}")
print(f"Total Sell Volume for for combined stratergies: {total_sell_volume_1}")


#Assignment 2

def compute_pnl(csv_file, strategy_id):
    total_pnl = 0

    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            if row['strategy'] == strategy_id:
                quantity = int(row['quantity'])
                price = float(row['price'])
                side = row['side']

                if side == 'buy':
                    income = -quantity * price
                elif side == 'sell':
                    income = quantity * price
                else:
                    income = 0  # Invalid side, ignore this row

                total_pnl += income
    
    return total_pnl

# Specify the CSV file name
csv_file_name = 'trades.csv'

# Specify the strategy id for which you want to calculate PnL
strategy_id = "strategy_2"

# Calculate and print the PnL for the specified strategy
pnl = compute_pnl(csv_file_name, strategy_id)
print(f"PnL for {strategy_id}: {pnl} euros")

#Assignment 3


app = Flask(__name__)
api = Api(app)


# Request parser for strategy_id
parser = reqparse.RequestParser()
parser.add_argument("strategy_id", type=str, required=True, help="string identifier of a strategy")

class PnL(Resource):
    def get(self, strategy_id):
        global csv_file_name
        print (csv_file_name, strategy_id, type(strategy_id))
        pnl2 = compute_pnl(csv_file_name, strategy_id)
        return {
            "strategy": strategy_id,
            "value": pnl2,
            "unit": "euro",
            "capture_time": "2023-01-16T08:15:46Z",
        }, 200

# Add the resource to the API with the specified path
api.add_resource(PnL, "/v1/pnl/<string:strategy_id>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
