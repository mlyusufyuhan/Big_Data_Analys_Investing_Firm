import matplotlib.pyplot as plt
import numpy as np

# Data
pink_cab_revenue = 26328251.33
pink_cab_profit = 5307328.321
yellow_cab_revenue = 125853887.19
yellow_cab_profit = 44020373.17079997

# Create the bar chart
labels = ['Pink Cab', 'Yellow Cab']
revenues = [pink_cab_revenue, yellow_cab_revenue]
profits = [pink_cab_profit, yellow_cab_profit]

x = range(len(labels))

fig, ax = plt.subplots(figsize=(10,6))

ax.bar(x, revenues, width=0.4, align='center', label='Revenue')
ax.bar([i+0.4 for i in x], profits, width=0.4, align='center', label='Profit')

plt.xticks(x, labels)
plt.ylabel('Amount in USD')
plt.title('Revenue and Profit of Pink Cab and Yellow Cab')
plt.legend()

plt.show()


pink_revenue = [7908479.23, 9578629.54, 8841142.56]
pink_profit = [1713511.224, 2033654.908, 1560162.189]

# Data for Yellow Cab
yellow_revenue = [38481133.18, 45818910.04, 41553843.97]
yellow_profit = [1.392700e+07, 1.657598e+07, 1.351740e+07]

# Years
years = [2016, 2017, 2018]

# Create a line graph
plt.plot(years, pink_revenue, label='Pink Cab Revenue')
plt.plot(years, pink_profit, label='Pink Cab Profit')
plt.plot(years, yellow_revenue, label='Yellow Cab Revenue')
plt.plot(years, yellow_profit, label='Yellow Cab Profit')

# Add title and axis labels
plt.title('Cab Revenue and Profit')
plt.xlabel('Year')
plt.ylabel('Amount')

# Add a legend
plt.legend()

# Show the graph
plt.show()

# Data for Pink Cab
pink_data = [37480, 47231]

# Data for Yellow Cab
yellow_data = [116000, 158681]

# Labels for x-axis
labels = ['Female', 'Male']

# Create bars
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
pink_bars = ax.bar(x - width/2, pink_data, width, label='Pink Cab')
yellow_bars = ax.bar(x + width/2, yellow_data, width, label='Yellow Cab')

# Add title and axis labels
ax.set_title('Number of Customers by Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Number of Customers')

# Add x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(labels)

# Add legend
ax.legend()

# Show the graph
plt.show()

# Data for Pink Cab
pink_data = [563509.67, 685823.52, 661739.92]

# Data for Yellow Cab
yellow_data = [1859978.21, 2214879.02, 2124560.24]

# Labels for x-axis
labels = ['2016', '2017', '2018']

# Create bars
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
pink_bars = ax.bar(x - width/2, pink_data, width, label='Pink Cab')
yellow_bars = ax.bar(x + width/2, yellow_data, width, label='Yellow Cab')

# Add title and axis labels
ax.set_title('Yearly Distance Covered by Cab Company')
ax.set_xlabel('Year')
ax.set_ylabel('Distance Covered (in km)')

# Add x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(labels)

# Add legend
ax.legend()

# Show the graph
plt.show()

year = [2016, 2017, 2018]
pink_cab = [16661, 18643, 18400]
yellow_cab = [25937, 27789, 27470]

# Plot
plt.bar(year, pink_cab, label='Pink Cab', color='pink')
plt.bar(year, yellow_cab, label='Yellow Cab', color='yellow', bottom=pink_cab)

# Axis labels
plt.xlabel('Year')
plt.ylabel('Number of Customers')
plt.title('Customers Covered by Pink Cab and Yellow Cab')

# Legend
plt.legend()

# Show plot
plt.show()

# data
pink_cab_users = {
    'ATLANTA GA': 1762,
    'AUSTIN TX': 1868,
    'BOSTON MA': 5186,
    'CHICAGO IL': 9361,
    'DALLAS TX': 1380,
    'DENVER CO': 1394,
    'LOS ANGELES CA': 19865,
    'MIAMI FL': 2002,
    'NASHVILLE TN': 1841,
    'NEW YORK NY': 13967,
    'ORANGE COUNTY': 1513,
    'PHOENIX AZ': 864,
    'PITTSBURGH PA': 682,
    'SACRAMENTO CA': 1334,
    'SAN DIEGO CA': 10672,
    'SEATTLE WA': 2732,
    'SILICON VALLEY': 3797,
    'TUCSON AZ': 799,
    'WASHINGTON DC': 3692
}

# create bar chart for Pink Cab users
fig, ax = plt.subplots()
ax.bar(pink_cab_users.keys(), pink_cab_users.values(), color='pink')
ax.set_title('Pink Cab Unique Users')
ax.set_xlabel('City')
ax.set_ylabel('Number of Users')
ax.set_xticklabels(pink_cab_users.keys(), rotation=90)

plt.show()

yellow_cab_users = {
    'ATLANTA GA': 5795,
    'AUSTIN TX': 3028,
    'BOSTON MA': 24506,
    'CHICAGO IL': 47264,
    'DALLAS TX': 5637,
    'DENVER CO': 2431,
    'LOS ANGELES CA': 28168,
    'MIAMI FL': 4452,
    'NASHVILLE TN': 1169,
    'NEW YORK NY': 85918,
    'ORANGE COUNTY': 2469,
    'PHOENIX AZ': 1200,
    'PITTSBURGH PA': 631,
    'SACRAMENTO CA': 1033,
    'SAN DIEGO CA': 9816,
    'SEATTLE WA': 5265,
    'SILICON VALLEY': 4722,
    'TUCSON AZ': 1132,
    'WASHINGTON DC': 40045
}

# create bar chart for Yellow Cab users
fig, ax = plt.subplots()
ax.bar(yellow_cab_users.keys(), yellow_cab_users.values(), color='yellow')
ax.set_title('Yellow Cab Unique Users')
ax.set_xlabel('City')
ax.set_ylabel('Number of Users')
ax.set_xticklabels(yellow_cab_users.keys(), rotation=90)

plt.show()

# Data
seasons = ['Fall 2016', 'Fall 2017', 'Fall 2018', 'Spring 2017', 'Spring 2018', 'Summer 2016', 'Summer 2017', 'Summer 2018', 'Winter 2016', 'Winter 2017', 'Winter 2018']
years = [2016, 2017, 2018, 2017, 2018, 2016, 2017, 2018, 2016, 2017, 2018]
profit_pink_cab = [669596.170, 755647.754, 575954.644, 272522.171, 209062.415, 228080.163, 361572.872, 252689.404, 815834.891, 643912.111, 522455.726]
profit_yellow_cab = [4.136139e+06, 4.956583e+06, 3.909493e+06, 3.961706e+06, 3.104921e+06, 2.057645e+06, 3.365564e+06, 2.806840e+06, 7.733212e+06, 4.292124e+06, 3.696146e+06]

# Set the bar width
bar_width = 0.35

# Set the positions of the x ticks
x_pos = np.arange(len(seasons))

# Create the figure and the axes
fig, ax = plt.subplots()

# Create a bar chart for Pink Cab and Yellow Cab profit
rects1 = ax.bar(x_pos - bar_width/2, profit_pink_cab, bar_width, label='Pink Cab', color='pink')
rects2 = ax.bar(x_pos + bar_width/2, profit_yellow_cab, bar_width, label='Yellow Cab', color='yellow')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Season-Year')
ax.set_ylabel('Profit')
ax.set_title('Profit Comparison between Pink Cab and Yellow Cab')
ax.set_xticks(x_pos)
ax.set_xticklabels(seasons)
ax.legend()

plt.show()


seasons = ['Fall', 'Spring', 'Summer', 'Winter']
distance_pink_cab = [703116.49, 210064.92, 412335.94, 585555.76]
distance_yellow_cab = [2009161.09, 834005.44, 1325661.99, 2030588.95]

# Create a pie chart for Pink Cab
fig, ax = plt.subplots()
ax.pie(distance_pink_cab, labels=seasons, autopct='%1.1f%%', startangle=90)
ax.set_title('Distance Covered by Pink Cab')

# Create a pie chart for Yellow Cab
fig, ax = plt.subplots()
ax.pie(distance_yellow_cab, labels=seasons, autopct='%1.1f%%', startangle=90)
ax.set_title('Distance Covered by Yellow Cab')

plt.show()


avg_distance = [22.56, 22.57]
avg_profit = [62.65, 160.26]
labels = ['Pink Cab', 'Yellow Cab']

# create pie chart for average customer distance
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].pie(avg_distance, labels=labels, autopct='%1.1f%%', startangle=90)
ax[0].set_title('Average Customer Distance')

# create pie chart for average customer profit
ax[1].pie(avg_profit, labels=labels, autopct='%1.1f%%', startangle=90)
ax[1].set_title('Average Customer Profit')

plt.show()

labels = ['NEW YORK NY', 'CHICAGO IL', 'LOS ANGELES CA', 'MIAMI FL', 'SILICON VALLEY', 
          'ORANGE COUNTY', 'SAN DIEGO CA', 'PHOENIX AZ', 'DALLAS TX', 'ATLANTA GA',
          'DENVER CO', 'AUSTIN TX', 'SEATTLE WA', 'TUCSON AZ', 'SAN FRANCISCO CA', 
          'SACRAMENTO CA', 'PITTSBURGH PA', 'WASHINGTON DC', 'NASHVILLE TN', 'BOSTON MA']
sizes = [3.59, 8.41, 9.04, 1.32, 2.31, 1.26, 7.30, 0.65, 2.35, 3.03, 1.65, 
         2.14, 3.73, 0.90, 33.93, 1.29, 0.67, 30.32, 2.83, 32.14]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#a3acff','#ffb3e6',
          '#c2c2f0','#ffb3b3','#c2d6d6','#e6b3b3','#e6e6e6','#ccf2ff',
          '#ffffcc','#d1e0e0','#ffc266','#f0c2d6','#b3ffb3','#b3b3ff',
          '#b3d9ff','#ffb3ff']

# Create pie chart
fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.title('Cab Users by City', fontsize=18)

# Show the chart
plt.show()

labels = ['NEW YORK NY', 'CHICAGO IL', 'LOS ANGELES CA', 'MIAMI FL', 'SILICON VALLEY', 
          'ORANGE COUNTY', 'SAN DIEGO CA', 'PHOENIX AZ', 'DALLAS TX', 'ATLANTA GA',
          'DENVER CO', 'AUSTIN TX', 'SEATTLE WA', 'TUCSON AZ', 'SAN FRANCISCO CA', 
          'SACRAMENTO CA', 'PITTSBURGH PA', 'WASHINGTON DC', 'NASHVILLE TN', 'BOSTON MA']
sizes = [3.59, 8.41, 9.04, 1.32, 2.31, 1.26, 7.30, 0.65, 2.35, 3.03, 1.65, 
         2.14, 3.73, 0.90, 33.93, 1.29, 0.67, 30.32, 2.83, 32.14]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#a3acff','#ffb3e6',
          '#c2c2f0','#ffb3b3','#c2d6d6','#e6b3b3','#e6e6e6','#ccf2ff',
          '#ffffcc','#d1e0e0','#ffc266','#f0c2d6','#b3ffb3','#b3b3ff',
          '#b3d9ff','#ffb3ff']

# Create pie chart
fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.title('Cab Users by City', fontsize=18)

# Show the chart
plt.show()

companies = ['Pink Cab', 'Yellow Cab']
profit_margins = [20.16, 34.98]
 
# Creating plot
fig = plt.figure(figsize=(10, 5))
 
# Create horizontal bars
plt.bar(companies, profit_margins)
 
# Add title and axis labels
plt.title('Profit Margin by Company')
plt.xlabel('Company')
plt.ylabel('Profit Margin')
 
# Show plot
plt.show()