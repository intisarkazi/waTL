from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

#mapbox is the platform that displays the plots created by plotly library

# LOADING BASEMAP

# LOADING CONSTRAINT JSON FILES
#for now load one file
#https://www.geeksforgeeks.org/read-json-file-using-python/

fpath = r"C:\Users\chand\Desktop\ICPxWP\Sample_data\T1\JSON\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_GeoJSON\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public.geojson"
fn = open(fpath)
data = json.load(fn)
df = pd.read_csv(fn)

# PLOTTING with mapbox
fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# BUFFERING 

# INSERTING COORDINATE POINTS

# FORMAT AS A HEATMAP