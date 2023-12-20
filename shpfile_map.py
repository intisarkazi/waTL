import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import geopandas as gpd
#import seaborn as sns #stat data visualisation

# LOADING BASEMAP

# LOADING CONSTRAINT SHP FILES
#for now load one file
T1_path = r"C:\Users\chand\Desktop\ICPxWP\Sample_data\T1\Legislated_Lands_and_Waters_DBCA_011_WA_GDA2020_Public_Shapefile\Legislated_Lands_and_Waters_DBCA_011.shp"
T2_path = r"C:\Users\chand\Desktop\ICPxWP\Sample_data\T2\Clearing_Regs_Enviro_Sensitive_Areas_DWER_046_WA_GDA2020_Public_Shapefile\Clearing_Regs_Enviro_Sensitive_Areas_DWER_046.shp"

# PLOTTING with geopandas
T1_df = gpd.read_file(T1_path)
T2_df = gpd.read_file(T2_path)

fig, ax = plt.subplots()

T1_df.plot(ax=ax, color='blue')
T2_df.plot(ax=ax, color='red')
plt.legend()
plt.show()

# BUFFERING 

# INSERTING COORDINATE POINTS

# FORMAT AS A HEATMAP
