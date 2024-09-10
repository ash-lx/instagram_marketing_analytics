import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Instagram Analytics Data
data = [
    {"S.no": 1, "Post type": "One product", "Age Range": "25-45", "Female": 100.0, "Male": 0.00, "Location": "Germany", "Accounts Reached": 283, "Profile Visit": 7, "Spent": 2.60, "Cost per profile visit": 0.37},
    {"S.no": 2, "Post type": "One product", "Age Range": "25-45", "Female": 100.0, "Male": 0.00, "Location": "Berlin, Hamburg, Frankfurt, Munich", "Accounts Reached": 268, "Profile Visit": 5, "Spent": 2.93, "Cost per profile visit": 0.59},
    {"S.no": 3, "Post type": "One product", "Age Range": "25-45", "Female": 100.0, "Male": 0.00, "Location": "Leipzig", "Accounts Reached": 396, "Profile Visit": 4, "Spent": 2.76, "Cost per profile visit": 0.69},
    {"S.no": 4, "Post type": "Multiple products", "Age Range": "25-45", "Female": 75.0, "Male": 25.00, "Location": "Germany", "Accounts Reached": 224, "Profile Visit": 2, "Spent": 3.02, "Cost per profile visit": 1.51},
    {"S.no": 5, "Post type": "Reel", "Age Range": "25-45", "Female": 75.0, "Male": 25.00, "Location": "Germany", "Accounts Reached": 318, "Profile Visit": 8, "Spent": 2.80, "Cost per profile visit": 0.35},
    {"S.no": 6, "Post type": "First customer", "Age Range": "18+", "Female": 85.0, "Male": 15.00, "Location": "Germany", "Accounts Reached": 201, "Profile Visit": 9, "Spent": 3.06, "Cost per profile visit": 0.34},
    {"S.no": 7, "Post type": "Product", "Age Range": "18+", "Female": 75.0, "Male": 25.00, "Location": "France + Germany", "Accounts Reached": 1290, "Profile Visit": 34, "Spent": 10.00, "Cost per profile visit": 0.29}
]

df = pd.DataFrame(data)

# Set consistent font and style
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
sns.set_style("whitegrid")

# Define a darker color palette
color_palette = ['#FFB347', '#FFA500', '#FF8C00', '#FF7F50', '#FF6347', '#FF4500', '#FF3300']

# 1. Overall Campaign Efficiency Overview
plt.figure(figsize=(12, 6))
bars = plt.bar(df['S.no'], df['Cost per profile visit'], color=color_palette)
plt.title('Cost per Profile Visit by Campaign', fontsize=16, fontweight='bold')
plt.xlabel('Campaign Number', fontsize=14)
plt.ylabel('Cost per Profile Visit (€)', fontsize=14)
plt.xticks(df['S.no'], fontsize=12)
plt.yticks(fontsize=12)
plt.grid(False)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'€{height:.2f}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

# 2. Geographic Efficiency Comparison (Updated)
# Calculate average for Germany
germany_avg = df[df['Location'] == 'Germany']['Cost per profile visit'].mean()

chart_data = pd.concat([chart_data, pd.DataFrame({
    'Location': ['Germany (Average)'],
    'Cost per profile visit': [germany_avg]
})], ignore_index=True)

# Sort the dataframe by Cost per profile visit
chart_data = chart_data.sort_values('Cost per profile visit', ascending=False)

plt.figure(figsize=(12, 6))
ax = sns.barplot(x='Location', y='Cost per profile visit', data=chart_data, palette=color_palette)
plt.title('Cost per Profile Visit by Location', fontsize=16, fontweight='bold')
plt.xlabel('Location', fontsize=14)
plt.ylabel('Cost per Profile Visit (€)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

for i, v in enumerate(chart_data['Cost per profile visit']):
    ax.text(i, v, f'€{v:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

# 3. Post Type Efficiency
plt.figure(figsize=(12, 6))
scatter = sns.scatterplot(x='Post type', y='Cost per profile visit', size='Profile Visit',
                          hue='Spent', data=df, sizes=(50, 500), palette='viridis')
plt.title('Post Type Efficiency', fontsize=16, fontweight='bold')
plt.xlabel('Post Type', fontsize=14)
plt.ylabel('Cost per Profile Visit (€)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

plt.legend(title='Spent (€)', title_fontsize='13', fontsize='11', bbox_to_anchor=(1.05, 1), loc='upper left')

for i, row in df.iterrows():
    plt.text(i, row['Cost per profile visit'], f'€{row["Cost per profile visit"]:.2f}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()