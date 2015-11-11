import overpass
from pprint import pprint
import json

# converts from unicode to ASCII encoding
def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

api = overpass.API()

coord_N = 37.7600  # center of district
coord_W = 122.4200
box_width = 0.03
south = coord_N - box_width/2
north = coord_N + box_width/2
west = -(coord_W + box_width/2)
east = -(coord_W - box_width/2)
print 'S=%s, W=%s, N=%s, E=%s' % (south, west, north, east)
# minimum latitude, minimum longitude, maximum latitude, maximum longitude (or South-West-North-East)
map_query = overpass.MapQuery(south, west, north, east)
response = api.Get(map_query)
pprint(convert(response))