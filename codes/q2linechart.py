import pandas as pd
import matplotlib.pyplot as plt

file_path = 'soru 2 data.csv'  
data = pd.read_csv(file_path)

countries = ['United States', 'India', 'China', 'Sweden']
filtered_data = data[data['Countries'].isin(countries)]

melted_data = filtered_data.melt(id_vars='Countries', var_name='Year', value_name='Meat Production')
melted_data['Year'] = melted_data['Year'].astype(int)

plt.figure(figsize=(12, 6))
for country in countries:
    country_data = melted_data[melted_data['Countries'] == country]
    plt.plot(country_data['Year'], country_data['Meat Production'], label=country, linewidth=2)

plt.title('Meat Production by Countries (1961-2022)')
plt.xlabel('Year')
plt.ylabel('Meat Production (tons)')
plt.legend(title='Countries')

plt.tight_layout()
plt.show()
