import pandas as pd
import plotly.express as px

file_path = 'soru 3 data.csv' 
data = pd.read_csv(file_path)

data = data[data['Year'] == 2022] 

fig = px.choropleth(
    data_frame=data,
    locations="Entity",  
    locationmode="country names",  
    color="Annual CO₂ emissions",  
    title="CO₂ Emissions by Country (2022)",
    color_continuous_scale=px.colors.sequential.YlOrRd,  
    range_color=(data["Annual CO₂ emissions"].min(), 1_000_000_000),  
    labels={'Annual CO₂ emissions': 'CO₂ Emissions (tons)'}  
)

fig.update_traces(hovertemplate='<b>%{location}</b>')
fig.show()
