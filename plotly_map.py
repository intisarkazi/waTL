from urllib.request import urlopen
import json
import pandas as pd
import geopandas as gpd
import plotly.express as px
import requests, getpass

#mapbox is the platform that displays the plots created by plotly library

# LOADING BASEMAP

# LOADING CONSTRAINT FILES

#for now load one file
#https://www.geeksforgeeks.org/read-json-file-using-python/

# fpath = r"C:\Users\chand\Desktop\ICPxWP\Sample_data\T1\JSON\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_GeoJSON\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public.geojson"
# fn = open(fpath)
# data = json.load(fn)
# df = pd.read_csv(fn)


#Automating data snapshot downloads
'''
def downloadData(folderName, fileName, userId, dataURL):

    #password = getpass.getpass()
    password= "Nunzoi88$"
    #rqst for an access token for authentication. Requested from a tokenRequestUrl using OAuth 2.0 password grant type
    tokenRequestUrl = "https://sso.slip.wa.gov.au/as/token.oauth2"
    tokenRequestHeaders = { 'Authorization' : 'Basic ZGlyZWN0LWRvd25sb2Fk'}
    tokenRequestForm={"grant_type": "password", "username":userId, "password":password}
    tokenResponse = requests.post(tokenRequestUrl, data=tokenRequestForm, headers=tokenRequestHeaders)
    accessToken=json.loads(tokenResponse.text)["access_token"]
    
    if tokenResponse.status_code == 200:
        dataDownloadRequestUrl = dataURL.format(folderName, fileName)
        print("Downloading file from URL: " + dataDownloadRequestUrl)
        dataDownloadRequestHeaders = { 'Authorization' : 'Bearer ' + accessToken}
        dataDownloadResponse = requests.get(dataDownloadRequestUrl, headers=dataDownloadRequestHeaders)
        
        if dataDownloadResponse.status_code == 200:
            #with open(fileName, 'wb') as f:
            #    f.write(dataDownloadResponse.content)
            #data = json.load(dataDownloadResponse)
            data = dataDownloadResponse.json()
            return data

        else:
            print("Error download file with error " + str(dataDownloadResponse.status_code) + "-" + dataDownloadResponse.text)
            return None
    else:
        print("Error getting token: " + str(tokenResponse.status_code) + "-" + tokenResponse.text)
        return None

dataURL= r"https://direct-download.slip.wa.gov.au/datadownload/Property_and_Planning/Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_GeoJSON.zip"
folderName = "Property_and_Planning"
fileName = "Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_GeoJSON.zip"
userId = "rehaab.syed@student.curtin.edu.au"
data = downloadData(folderName, fileName, userId, dataURL)
'''

#load file with geopandas
T1_path = r"C:\Users\chand\Desktop\ICPxWP\Sample_data\T1\JSON\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_GeoJSON\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public.geojson"
T1_df = gpd.read_file(T1_path)
#print(T1_df.columns)
'''
Index(['leg_pin', 'leg_poly_area', 'leg_class', 'leg_identifier',
       'leg_purpose', 'leg_vesting', 'leg_name', 'leg_name_status', 'leg_iucn',
       'leg_tenure', 'leg_act', 'leg_category', 'leg_notes',
       'leg_agreement_party', 'leg_classification', 'leg_regno',
       'st_area_shape_', 'st_perimeter_shape_', 'geometry'],
      dtype='object'). 
'''
#f'ig, ax = plt.subplots()

# PLOTTING with mapbox
fig = px.choropleth_mapbox(T1_df, geojson=T1_path, 
                           locations = T1_df['leg_identifier'], 
                           color_discrete_constant="red",
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# BUFFERING 

# INSERTING COORDINATE POINTS

# FORMAT AS A HEATMAP