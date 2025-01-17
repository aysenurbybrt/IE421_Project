import pandas as pd
import matplotlib.pyplot as plt

file_path = 'soru 1 data.csv' 
data = pd.read_csv(file_path)

data.rename(columns={'Total kgCO_eq per kg ': 'Emissions'}, inplace=True)

filtered_data = data[data['Emissions'] >= 1]

sorted_data = filtered_data.sort_values(by='Emissions', ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(sorted_data['Entity'], sorted_data['Emissions'], color='#9e4312')

for index, value in enumerate(sorted_data['Emissions']):
    plt.text(value + 1, index, f"{value} kg", va='center')

plt.title('CO2 Emissions from Foods')
plt.xlabel('Emissions (kg CO2 per kg of food)')
plt.ylabel('Entity')
plt.xlim(0, sorted_data['Emissions'].max() + 10)

plt.tight_layout()
plt.show()
