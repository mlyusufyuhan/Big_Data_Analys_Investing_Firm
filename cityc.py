import pandas as pd


cabdata = pd.read_csv('Cab_Data.csv')
TranID = pd.read_csv('Transaction_ID.csv')
customerID = pd.read_csv('Customer_ID.csv')
citiesdata = pd.read_csv('City.csv')

pink_cab_df = cabdata[cabdata['Company'] == 'Pink Cab']
pink_cab_user_counts = pink_cab_df.groupby('City')['Transaction ID'].nunique()
print('Pink Cab unique users:\n', pink_cab_user_counts)

# Unique users for Yellow Cab
yellow_cab_df = cabdata[cabdata['Company'] == 'Yellow Cab']
yellow_cab_user_counts = yellow_cab_df.groupby('City')['Transaction ID'].nunique()
print('Yellow Cab unique users:\n', yellow_cab_user_counts)

merged_df = pd.merge(TranID, customerID, on='Customer ID')
merged_df = pd.merge(merged_df, cabdata, on='Transaction ID')

# Filter transactions of Pink Cab
pink_cab_df = merged_df[merged_df['Company'] == 'Pink Cab']

# Group the data by gender and sum up the price charged and cost of trip for each group
gender_wise_df = pink_cab_df.groupby('Gender').agg({'Price Charged': 'sum', 'Cost of Trip': 'sum'})

# Calculate profit for each gender
gender_wise_df['Profit'] = gender_wise_df['Price Charged'] - gender_wise_df['Cost of Trip']

# Calculate the difference in profit between the genders
profit_diff = gender_wise_df.loc['Male', 'Profit'] - gender_wise_df.loc['Female', 'Profit']

print("Difference in profit between genders: ", profit_diff)

merged_df = pd.merge(TranID, customerID, on='Customer ID')
merged_df = pd.merge(merged_df, cabdata, on='Transaction ID')

# Filter transactions of Pink Cab
pink_cab_df = merged_df[merged_df['Company'] == 'Pink Cab']

# Calculate profit per km
pink_cab_df['Profit per KM'] = (pink_cab_df['Price Charged'] - pink_cab_df['Cost of Trip']) / pink_cab_df['KM Travelled']

# Group the data by distance traveled and calculate the average profit per km
distance_wise_df = pink_cab_df.groupby(pd.cut(pink_cab_df['KM Travelled'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])).agg({'Profit per KM': 'mean'})

# Calculate the average profit for long-range distances (above 50 KM) and short-range distances (below or equal to 50 KM)
long_range_profit_avg = pink_cab_df[pink_cab_df['KM Travelled'] > 30]['Profit per KM'].mean()
short_range_profit_avg = pink_cab_df[pink_cab_df['KM Travelled'] <= 30]['Profit per KM'].mean()

# Compare the average profit for long-range and short-range distances
if long_range_profit_avg > short_range_profit_avg:
    print("On average, Pink Cab generates higher profit per KM for long-range distances.")
elif long_range_profit_avg < short_range_profit_avg:
    print("On average, Pink Cab generates higher profit per KM for short-range distances.")
else:
    print("On average, Pink Cab generates the same profit per KM for long-range and short-range distances.")

# Merge the dataframes
merged_df = pd.merge(TranID, customerID, on='Customer ID')
merged_df = pd.merge(merged_df, cabdata, on='Transaction ID')


merged_df['Profit'] = merged_df['Price Charged'] - merged_df['Cost of Trip']

# Group the merged dataframe by payment mode
payment_mode_groups = merged_df.groupby('Payment_Mode')

# Calculate the average profit for each payment mode group
payment_mode_profit = payment_mode_groups['Profit'].mean()

# Print the average profit for card and cash payment modes
print("Average profit for card payment mode:", payment_mode_profit['Card'])
print("Average profit for cash payment mode:", payment_mode_profit['Cash'])

pink_cab = cabdata[cabdata['Company'] == 'Pink Cab']
yellow_cab = cabdata[cabdata['Company'] == 'Yellow Cab']

# calculate total revenue and cost for each company
pink_cab_revenue = pink_cab['Price Charged'].sum()
pink_cab_cost = pink_cab['Cost of Trip'].sum()

yellow_cab_revenue = yellow_cab['Price Charged'].sum()
yellow_cab_cost = yellow_cab['Cost of Trip'].sum()

# calculate profit and profit margin for each company
pink_cab_profit = pink_cab_revenue - pink_cab_cost
pink_cab_margin = (pink_cab_profit / pink_cab_revenue) * 100

yellow_cab_profit = yellow_cab_revenue - yellow_cab_cost
yellow_cab_margin = (yellow_cab_profit / yellow_cab_revenue) * 100

# print the results
print('Pink Cab profit margin: {:.2f}%'.format(pink_cab_margin))
print('Yellow Cab profit margin: {:.2f}%'.format(yellow_cab_margin))