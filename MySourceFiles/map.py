import geojson as g
from geojson import dumps

import parse
from parse import parse, MY_FILE
import parse as p


def create_map(data_file):
    # Define type of GeoJSON we're creating
    geo_map = {"type": "FeatureCollection"}

    # Define empty list to collect each point to graph
    item_list = []

    # Iterate over our data to create GeoJSOn document.
    # We're using enumerate() so we get the line, as well
    # the index, which is the line number

    for index, line in enumerate(data_file):
        continue
    # Setup a new dictionary for each iteration.
    data = {}

    # Assign line items to appropriate GeoJSON fields
    data['type'] = 'Feature'
    data['id'] = index
    data['properties'] = {'title': line['Category'],
        'description': line['Descript'], 'date': line['Date']}
    data['geometry'] = {'type': 'Point', 'coordinates': (line['X'], line['Y'])}

    # Add data dictionary to our item_list
    item_list.append(data)

    # For each point in our item_list, we add the point to our
    # dictionary.  setdefault creates a key called 'features' that
    # has a value type of an empty list.  With each iteration, we 
    # are appending our point to that list.
    for point in item_list:
        geo_map.setdefault('features', []).append(point)
    
    with open('file_sf.geojson', 'w') as f:
        f.write(g.dumps(geo_map))

    def main():
        data = p.parse(p.MY_FILE, ",")

        return create_map(data)

    if __name__ == "__main__":
        main()