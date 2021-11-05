import math
import numpy as np

def lon_lat_to_distance(lat1, lon1, lat2, lon2):
    
    Earth_Radius = 6378.137 # approximate radius of earth in km
    
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = Earth_Radius * c
    return distance

def cal_edges(lat_range, lon_range, grid_dist):
    lat_dist = lon_lat_to_distance(lat_range[0], lon_range[0], lat_range[1], lon_range[0])
    lon_dist = lon_lat_to_distance(lat_range[0], lon_range[0], lat_range[0], lon_range[1])
    num_edges_lat = math.ceil(lat_dist * 1e3 / grid_dist)
    num_edges_lon = math.ceil(lon_dist * 1e3 / grid_dist)
    xedges = np.linspace(lat_range[0], lat_range[1], num=num_edges_lat)
    yedges = np.linspace(lon_range[0], lon_range[1], num=num_edges_lon)
    return xedges, yedges