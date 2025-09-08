import pandas as pd
import matplotlib as mlt
import matplotlib.pyplot as plt

# file_path = 'C:\Users\Employee Sample Data.csv'
df = pd.read_csv(r'C:\Users\Employee Sample Data.csv', encoding='ISO-8859-1')
print(df)

df['Annual Salary'] = df['Annual Salary'].replace(r'[\$,]', '', regex=True).astype(float)


# Plot a graph between Age and Annual Salary
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Annual Salary'], color='b', alpha=0.6)

# Add labels and title
plt.title('Scatter Plot: Age vs. Annual Salary', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Annual Salary (USD)', fontsize=12)
plt.grid(True)

# Show the plot
plt.show()
