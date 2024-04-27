import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key = "AIzaSyAY9ETnhPRgP3_z5FwlR6F2SYuZBjpKnfs")

from math import radians, sin, cos, asin, sqrt



radii=[]
for i in range(1,50):
    radii.append(i*1000)
all_outlets = []
for r in radii:

    results = gmaps.places_nearby(
        location=(12.971599,77.594566),
        radius=r,  # Adjust search radius in meters
        keyword="shopping and hangout in bangalore"  # Start with malls
    )

    for place in results['results']:
        address = place.get('vicinity','').split(',')[-1]
        all_outlets.append({
            'Name': place['name'],
            'Latitude': place['geometry']['location']['lat'], 
            'Longitude': place['geometry']['location']['lng'], 
            'City': address,
            'id':place['place_id']
            # Add more fields if needed
        })
    
    
dict = {"Bangalore":[12.971599, 77.594566],
        "Chennai":[13.0827, 80.2707],
        "Hyderabad":[17.4065, 78.4772],
        "New Delhi":[28.6139, 77.2090],
        "Ahmedabad":[23.0225, 72.5714],
        "Kolkata":[22.5726,88.3639],
        "Mumbai":[19.0760, 72.8777],
        "Noida":[28.5355, 77.3910],
        "Pune":[18.5204, 73.8567]}
# all = []

# for i in dict:
#     all.extend(get_outlet_data(dict[i][0],dict[i][1]))
    
df = pd.DataFrame(all_outlets) 
df = df.drop_duplicates(subset='id')
df.to_excel("blr.xlsx",index=False)
#print(df) 


# def get_outlet_data(gmaps, city_name, brand, radius, grid_spacing):
#     all_results = []
#     for lat in range(start_latitude, end_latitude, grid_spacing):
#         for lng in range(start_longitude, end_longitude, grid_spacing):
#             center = (lat, lng)
#             results = gmaps.places_nearby(
#                 keyword=brand + " " + city_name,  # Combine brand and city
#                 location=center,
#                 radius=radius
#             )
#             if results['results']:
#                 for result in results['results']:
#                     data = {
#                         'Brand': brand,
#                         'Name': result['name'],
#                         'Latitude': result['geometry']['location']['lat'],
#                         'Longitude': result['geometry']['location']['lng'],
#                         'City': city_name
#                     }
#                     all_results.append(data)
#     return all_results



