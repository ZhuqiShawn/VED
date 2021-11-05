import os
import pandas as pd
import numpy as np

def file_list(path):
    fileList = os.listdir(path)
    for file in fileList:
        name = file.split('.')
        if name[-1] != 'csv':
            fileList.remove(file)
    return len(fileList), fileList

def read_lat_lon(file):
    data = pd.read_csv(file)
    try:
        lat, lon = data["Latitude[deg]"], data["Longitude[deg]"]
    except KeyError as err:
        raise KeyError("Error {} - No column Latitude[deg] or Longitude[deg]".format(err))
    lat_range = (np.min(lat), np.max(lat))
    lon_range = (np.min(lon), np.max(lon))
    return lat_range, lon_range, lat, lon