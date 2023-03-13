import pandas as pd
import csv

cabdata = pd.read_csv('Cab_Data.csv')
TranID = pd.read_csv('Transaction_ID.csv')
customerID = pd.read_csv('Customer_ID.csv')
citiesdata = pd.read_csv('City.csv')

trans_count = cabdata['Company'].value_counts()
print(trans_count['Pink Cab'])
print(trans_count['Yellow Cab'])

pink_cab = cabdata[cabdata['Company'] == 'Pink Cab']
yellow_cab = cabdata[cabdata['Company'] == 'Yellow Cab']

# Calculate revenue and profit for Pink Cab
pink_cab_revenue = pink_cab['Price Charged'].sum()
pink_cab_cost = pink_cab['Cost of Trip'].sum()
pink_cab_profit = pink_cab_revenue - pink_cab_cost

# Calculate revenue and profit for Yellow Cab
yellow_cab_revenue = yellow_cab['Price Charged'].sum()
yellow_cab_cost = yellow_cab['Cost of Trip'].sum()
yellow_cab_profit = yellow_cab_revenue - yellow_cab_cost

print('Pink Cab Revenue:', pink_cab_revenue)
print('Pink Cab Profit:', pink_cab_profit)

print('Yellow Cab Revenue:', yellow_cab_revenue)
print('Yellow Cab Profit:', yellow_cab_profit)

# Convert the 'Date of Travel' column to datetime
cabdata['Date of Travel'] = pd.to_datetime(cabdata['Date of Travel'])

# Extract year from the 'Date of Travel' column and create a new column 'Year'
cabdata['Year'] = cabdata['Date of Travel'].dt.year

# Group data by company and year
pink_data = cabdata[cabdata['Company'] == 'Pink Cab']
pink_revenue = pink_data.groupby('Year')['Price Charged'].sum()
pink_cost = pink_data.groupby('Year')['Cost of Trip'].sum()
pink_profit = pink_revenue - pink_cost

yellow_data = cabdata[cabdata['Company'] == 'Yellow Cab']
yellow_revenue = yellow_data.groupby('Year')['Price Charged'].sum()
yellow_cost = yellow_data.groupby('Year')['Cost of Trip'].sum()
yellow_profit = yellow_revenue - yellow_cost

print('Pink Cab yearly revenue:\n', pink_revenue)
print('Pink Cab yearly profit:\n', pink_profit)

print('Yellow Cab yearly revenue:\n', yellow_revenue)
print('Yellow Cab yearly profit:\n', yellow_profit)

df = pd.merge(customerID, TranID, on='Customer ID')
df = pd.merge(df, cabdata, on='Transaction ID')

groups = df.groupby(['Company', 'Gender'])

# Counting the number of male and female customers for each company
counts = groups['Transaction ID'].count()

# Extracting the counts for Pink Cab and Yellow Cab
pink_cab_counts = counts.loc['Pink Cab']
yellow_cab_counts = counts.loc['Yellow Cab']

# Printing the results
print("Pink Cab:\n", pink_cab_counts, "\n")
print("Yellow Cab:\n", yellow_cab_counts)

citiesdata['Population'] = citiesdata['Population'].str.replace(',', '').astype(int)
citiesdata['Users'] = citiesdata['Users'].str.replace(',', '').astype(int)

cabdata['KM Travelled'] = cabdata['KM Travelled'].round(2)

# merge transaction_df with cab_df on Transaction ID
transaction_cab_df = pd.merge(TranID, cabdata, on='Transaction ID')

# merge transaction_cab_df with city_df on City
transaction_cab_city_df = pd.merge(transaction_cab_df, citiesdata, on='City')

# merge transaction_cab_city_df with customer_df on Customer ID
final_df = pd.merge(transaction_cab_city_df, customerID, on='Customer ID')

final_df['Year'] = pd.to_datetime(final_df['Date of Travel']).dt.year

# calculate the distance covered for each trip
final_df['Distance Covered'] = final_df['KM Travelled']

# create a pivot table to get city-wise cab user covered by Pink Cab and Yellow Cab


# create a pivot table to get yearly distance covered by Pink Cab and Yellow Cab
pivot_table2 = pd.pivot_table(final_df, values='Distance Covered', index='Year', columns='Company', aggfunc='sum')
print('\nYearly distance covered by Pink Cab and Yellow Cab:')
print(pivot_table2)

# create a pivot table to get year-wise customer covered by Pink Cab and Yellow Cab
pivot_table3 = pd.pivot_table(final_df, values='Customer ID', index='Year', columns='Company', aggfunc=pd.Series.nunique)
print('\nYear-wise customer covered by Pink Cab and Yellow Cab:')
print(pivot_table3)


user_counts = final_df.groupby('City')['Transaction ID'].nunique()
print(user_counts)


# Filter data for Pink Cab and Yellow Cab
pink_cab_data = cabdata[cabdata['Company'] == 'Pink Cab']
yellow_cab_data = cabdata[cabdata['Company'] == 'Yellow Cab']

# Convert the 'Date of Travel' column to datetime
pink_cab_data['Date of Travel'] = pd.to_datetime(pink_cab_data['Date of Travel'])
yellow_cab_data['Date of Travel'] = pd.to_datetime(yellow_cab_data['Date of Travel'])

# Extract year from the 'Date of Travel' column and create a new column 'Year'
pink_cab_data['Year'] = pink_cab_data['Date of Travel'].dt.year
yellow_cab_data['Year'] = yellow_cab_data['Date of Travel'].dt.year

# Calculate revenue and profit for Pink Cab by year
pink_cab_revenue_by_year = pink_cab_data.groupby('Year')['Price Charged'].sum()
pink_cab_cost_by_year = pink_cab_data.groupby('Year')['Cost of Trip'].sum()
pink_cab_profit_by_year = pink_cab_revenue_by_year - pink_cab_cost_by_year

# Calculate revenue and profit for Yellow Cab by year
yellow_cab_revenue_by_year = yellow_cab_data.groupby('Year')['Price Charged'].sum()
yellow_cab_cost_by_year = yellow_cab_data.groupby('Year')['Cost of Trip'].sum()
yellow_cab_profit_by_year = yellow_cab_revenue_by_year - yellow_cab_cost_by_year

# Calculate revenue and profit growth for Pink Cab by year
pink_cab_revenue_growth = pink_cab_revenue_by_year.pct_change() * 100
pink_cab_profit_growth = pink_cab_profit_by_year.pct_change() * 100

# Calculate revenue and profit growth for Yellow Cab by year
yellow_cab_revenue_growth = yellow_cab_revenue_by_year.pct_change() * 100
yellow_cab_profit_growth = yellow_cab_profit_by_year.pct_change() * 100

# Print the results
print('Pink Cab Revenue Growth:\n', pink_cab_revenue_growth)
print('Pink Cab Profit Growth:\n', pink_cab_profit_growth)

print('Yellow Cab Revenue Growth:\n', yellow_cab_revenue_growth)
print('Yellow Cab Profit Growth:\n', yellow_cab_profit_growth)




# calculate profit for each ride
cabdata['Profit'] = cabdata['Price Charged'] - cabdata['Cost of Trip']

# create a dictionary to map months to seasons
month_to_season = {12: 'Winter', 1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
                   6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall', 11: 'Fall'}

# create a new column for season
cabdata['Season'] = cabdata['Date of Travel'].dt.month.map(month_to_season)

# calculate seasonal profit for Pink Cab
pink_cab_seasonal_profit = cabdata[cabdata['Company']=='Pink Cab'].groupby(['Season', cabdata['Date of Travel'].dt.year]).sum()['Profit'].reset_index()
pink_cab_seasonal_profit.rename(columns={'Date of Travel': 'Year', 'Profit': 'Profit_Pink Cab'}, inplace=True)

# calculate seasonal profit for Yellow Cab
yellow_cab_seasonal_profit = cabdata[cabdata['Company']=='Yellow Cab'].groupby(['Season', cabdata['Date of Travel'].dt.year]).sum()['Profit'].reset_index()
yellow_cab_seasonal_profit.rename(columns={'Date of Travel': 'Year', 'Profit': 'Profit_Yellow Cab'}, inplace=True)

# merge the two seasonal profit dataframes
seasonal_profit = pd.merge(pink_cab_seasonal_profit, yellow_cab_seasonal_profit, on=['Season', 'Year'], how='outer')

# fill NaN values with 0
seasonal_profit.fillna(0, inplace=True)

# display the results
print(seasonal_profit)

# calculate distance covered for each ride
cabdata['Distance Covered'] = cabdata['KM Travelled']

# create a new column for season
cabdata['Season'] = cabdata['Date of Travel'].dt.month.map(month_to_season)

# calculate distance covered by season for Pink Cab
pink_cab_seasonal_distance = cabdata[cabdata['Company']=='Pink Cab'].groupby(['Season', 'Date of Travel']).sum()['Distance Covered'].reset_index()
pink_cab_seasonal_distance = pink_cab_seasonal_distance.groupby('Season').sum()['Distance Covered'].reset_index()

# calculate distance covered by season for Yellow Cab
yellow_cab_seasonal_distance = cabdata[cabdata['Company']=='Yellow Cab'].groupby(['Season', 'Date of Travel']).sum()['Distance Covered'].reset_index()
yellow_cab_seasonal_distance = yellow_cab_seasonal_distance.groupby('Season').sum()['Distance Covered'].reset_index()

# merge the two seasonal distance dataframes
seasonal_distance = pd.merge(pink_cab_seasonal_distance, yellow_cab_seasonal_distance, on='Season', suffixes=('_Pink Cab', '_Yellow Cab'))

# display the results
print(seasonal_distance)

pink_cab_avg_distance = cabdata[cabdata['Company']=='Pink Cab']['KM Travelled'].mean()

# calculate average customer distance for Yellow Cab
yellow_cab_avg_distance = cabdata[cabdata['Company']=='Yellow Cab']['KM Travelled'].mean()

# display the results
print('Average customer distance for Pink Cab: {:.2f} km'.format(pink_cab_avg_distance))
print('Average customer distance for Yellow Cab: {:.2f} km'.format(yellow_cab_avg_distance))


pink_cab_profit = cabdata[cabdata['Company'] == 'Pink Cab']['Profit'].sum()
yellow_cab_profit = cabdata[cabdata['Company'] == 'Yellow Cab']['Profit'].sum()

# calculate total number of customers served by each cab company
pink_cab_customers = len(cabdata[cabdata['Company'] == 'Pink Cab']['Transaction ID'].unique())
yellow_cab_customers = len(cabdata[cabdata['Company'] == 'Yellow Cab']['Transaction ID'].unique())

# calculate average customer profit for each cab company
avg_pink_cab_profit = pink_cab_profit / pink_cab_customers
avg_yellow_cab_profit = yellow_cab_profit / yellow_cab_customers

# display the results
print("Average customer profit for Pink Cab: ${:.2f}".format(avg_pink_cab_profit))
print("Average customer profit for Yellow Cab: ${:.2f}".format(avg_yellow_cab_profit))

city_data = [
    {'City': 'NEW YORK NY', 'Population': 8405837, 'Cab Users': 302149},
    {'City': 'CHICAGO IL', 'Population': 1955130, 'Cab Users': 164468},
    {'City': 'LOS ANGELES CA', 'Population': 1595037, 'Cab Users': 144132},
    {'City': 'MIAMI FL', 'Population': 1339155, 'Cab Users': 17675},
    {'City': 'SILICON VALLEY', 'Population': 1177609, 'Cab Users': 27247},
    {'City': 'ORANGE COUNTY', 'Population': 1030185, 'Cab Users': 12994},
    {'City': 'SAN DIEGO CA', 'Population': 959307, 'Cab Users': 69995},
    {'City': 'PHOENIX AZ', 'Population': 943999, 'Cab Users': 6133},
    {'City': 'DALLAS TX', 'Population': 942908, 'Cab Users': 22157},
    {'City': 'ATLANTA GA', 'Population': 814885, 'Cab Users': 24701},
    {'City': 'DENVER CO', 'Population': 754233, 'Cab Users': 12421},
    {'City': 'AUSTIN TX', 'Population': 698371, 'Cab Users': 14978},
    {'City': 'SEATTLE WA', 'Population': 671238, 'Cab Users': 25063},
    {'City': 'TUCSON AZ', 'Population': 631442, 'Cab Users': 5712},
    {'City': 'SAN FRANCISCO CA', 'Population': 629591, 'Cab Users': 213609},
    {'City': 'SACRAMENTO CA', 'Population': 545776, 'Cab Users': 7044},
    {'City': 'PITTSBURGH PA', 'Population': 542085, 'Cab Users': 3643},
    {'City': 'WASHINGTON DC', 'Population': 418859, 'Cab Users': 127001},
    {'City': 'NASHVILLE TN', 'Population': 327225, 'Cab Users': 9270},
    {'City': 'BOSTON MA', 'Population': 248968, 'Cab Users': 80021}
]

for city in city_data:
    percentage = (city['Cab Users'] / city['Population']) * 100
    print(f"{city['City']}: {percentage:.2f}%")




