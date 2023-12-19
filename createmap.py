import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import geopandas as gpd
#import seaborn as sns #stat data visualisation


# LOADING BASEMAP

# LOADING CONSTRAINT SHP FILES

#for now load one file
shp_path = r"C:\Users\chand\Desktop\ICPxWP\Sample_data\T1\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_Shapefile\Legislated_Lands_and_Waters_DBCA_011.shp"

#read shape file
sf = shp.Reader(shp_path)

#convert shp -> pandas df
def read_shapefile(sf):
    #fetching the headings from the shape file
    fields = [x[0] for x in sf.fields][1:]

    #fetching the records from the shape file
    records = [list(i) for i in sf.records()]
    shps = [s.points for s in sf.shapes()]

    #converting shapefile data into pandas dataframe
    df = pd.DataFrame(columns=fields, data=records)

    #assigning the coordinates
    df = df.assign(coords=shps)

    return df
 
# PLOTTING
def plot_map(sf, x_lim = None, y_lim = None, figsize = (11,9)):
    plt.figure(figsize = figsize)
    id=0
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')
        
        # if (x_lim == None) & (y_lim == None):
        #     x0 = np.mean(x)
        #     y0 = np.mean(y)
        #     plt.text(x0, y0, id, fontsize=10)
        id = id+1
    
    if (x_lim != None) & (y_lim != None):     
        plt.xlim(x_lim)
        plt.ylim(y_lim)
    plt.show()

#calling the function and passing required parameters to plot the full map
#plot_map(sf)

# trying with geopandas
map_df = gpd.read_file(shp_path)
map_df.plot()
plt.show()



# BUFFERING 

# INSERTING COORDINATE POINTS

# FORMAT AS A HEATMAP
