from math import radians, cos, sin, asin, sqrt
import numpy as np
class Mobile_app(insert,system):

    def __init__(self):
        pass

    def column(matrix, i):
        return [row[i] for row in matrix]

    def find_nearest_parking():
        park_list=super.request("parking_list")
        c2=column(park_list,2)
        c1=column(park_list,1)

        center = (lon, lat)
        points = np.column_stack((c2,c1)) #"points = [(lon1, lat1), (lon2, lat2), (lon3, lat3), (lon4, lat4), (lon5, lat5))"

        altogether = [list(center) + list(item) for item in points]
        global distances
        distances = list(map(lambda a: haversine(*a), altogether))
        return

    def haversine(lon1, lat1, lon2, lat2):
        #"""
        #Calculate the great circle distance between two points
        #on the earth (specified in decimal degrees)
        #"""
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r
