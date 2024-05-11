import matplotlib.pyplot as plt 
import pandas as pd 
labels=['kcr','mns','myb','bfs','mtr','star'] 
values=[10,30,45,20,30,40] 
colors=['yellow','green','red','blue','pink','orange'] 
explode=[0,0,0,0,0,0] 
plt.title('A pie chart for mobile brand') 
plt.pie(values,labels=labels,colors=colors,explode=explode,startangle=180) 
data={'redflower':[1,3,4,3,5], 
 'yellow flower':[2,4,5,2,4], 
 'white flower':[3,2,3,1,3]} 
# Plot using data frame 
df=pd.DataFrame(data) 
df.plot(kind='bar') 
df.plot(kind='bar',stacked=True) 
plt.show()




# Sample data
categories = ['kcr', 'mtr', ' myb','mns','bfs','star']
values1 = [10, 15, 20, 34,23,45]
# Define the width of the bars
bar_width = 0.35
# Create the figure and the axes
fig, ax = plt.subplots()
# Define the x locations for the groups
x = range(len(categories))
# Plot the first set of bars
bars1 = ax.bar(x, values1, width=bar_width, label='Group 1')
# Plot the second set of bars, shifting the x positions
#bars2 = ax.bar([i + bar_width for i in x], values1, width=bar_width, label='Group 2')
# Set labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Clustered Column Chart')
ax.set_xticks([i + bar_width / 2 for i in x])
ax.set_xticklabels(categories)
ax.legend()
# Show plot
plt.show()
# Sample data
labels = ['red', 'green', 'yellow', 'whiteflo']
sizes = [15, 30, 45, 10]
# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
import matplotlib.pyplot as plt
# Sample data
labels = ['red', 'green', 'yellow', 'whiteflo']
sizes = [15, 30, 45, 10]
# Create donut chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Donut Chart')
plt.gca().add_artist(plt.Circle((0,0),0.70,fc='white'))  # Add a circle at the center to make it a donut
plt.axis('equal')
plt.show()
import pandas as pd
# Sample data
data = {'Name': ['red', 'green', 'yellow', 'whiteflo'],
   'weight': [25, 30, 35, 40,],
  'tot cost': [50000, 60000, 70000, 80000]}
# Create DataFrame
df = pd.DataFrame(data)
# Display as a table
print(df)
import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
# Create scatter chart
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Data points')
plt.title('Scatter Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
