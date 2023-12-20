from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px
import requests, getpass

#mapbox is the platform that displays the plots created by plotly library

# LOADING BASEMAP

# LOADING CONSTRAINT FILES

#for now load one file
#https://www.geeksforgeeks.org/read-json-file-using-python/
'''
fpath = r"C:\Users\chand\Desktop\ICPxWP\Sample_data\T1\JSON\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_GeoJSON\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public.geojson"
fn = open(fpath)
data = json.load(fn)
df = pd.read_csv(fn)
'''

#Automating data snapshot downloads

def downloadData(folderName, fileName, userId, dataURL):

    password = getpass.getpass()

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
            data = json.load(dataDownloadResponse)

        else:
            print("Error download file with error " + str(dataDownloadResponse.status_code) + "-" + dataDownloadResponse.text)
    else:
        print("Error getting token: " + str(tokenResponse.status_code) + "-" + tokenResponse.text)

    return data

dataURL= https://direct-download.slip.wa.gov.au/datadownload/Property_and_Planning/Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_GeoJSON.zip
folderName = "Property_and_Planning"
fileName = "Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_GeoJSON.zip"
userId = "rehaab.syed@student.curtin.edu.au"
data = downloadData(folderName, fileName, userId, dataURL)

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