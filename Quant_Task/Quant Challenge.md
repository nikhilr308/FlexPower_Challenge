# Quant Challenge

Before running the code:

Make sure that the code and SQL files are in the same folder.
Install the Flask and flask_restful libraries.

# Task 1:

The database named trades in the trades.sqlite file contains the table epex_12_20_12_13, not epex_2022_12_20_12-13.
The code converts the two tables in the database to CSV files.
The output of Task 1 contains 6 different outputs, of which 4 determine the total buy/sell volume for each strategy and the 2 other outputs determine the total buy/sell volume for the combination of both strategies. This is because it is not clear from the instructions which total buy/sell volume needs to be calculated.

# Task 2:

Specify the strategy name for "flex power" for which you want to calculate PnL in the code.

# Task 3:

To get the output of Task 2, copy the URL from the output followed by /v1/pnl/<string:strategy_id> and paste it into a browser. For example, if the strategy ID is strategy_2, the URL would be http://127.0.0.1:5000/v1/pnl/strategy_2.





