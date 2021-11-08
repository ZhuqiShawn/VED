import os
import pandas as pd
import numpy as np

def file_list(path):
    """This is a helper function for listing csv files in the given path

    Args:
        path (string): give the target path

    Returns:
        tuple: return the number of found csv files in the given path and a list of names of these files
    """
    fileList = os.listdir(path)
    for file in fileList:
        name = file.split('.')
        if name[-1] != 'csv':
            fileList.remove(file)
    return len(fileList), fileList

def read_lat_lon(file):
    """This is a function to read a csv file and extract the latitude and longitude columns

    Args:
        file (string): the name of target file

    Raises:
        KeyError: cannot found latitude or longitude columns in the given file

    Returns:
        tuple: latitude range, longitude range, latitude column, longitude column
    """
    data = pd.read_csv(file)
    try:
        lat, lon = data["Latitude[deg]"], data["Longitude[deg]"]
    except KeyError as err:
        raise KeyError("Error {} - No column Latitude[deg] or Longitude[deg]".format(err))
    lat_range = (np.min(lat), np.max(lat))
    lon_range = (np.min(lon), np.max(lon))
    return lat_range, lon_range, lat, lon