"""This module makes web-maps"""

def get_info_from_user():
    """
    Get information from user.
    ---------------------------------------------------
    No arguments.
    ---------------------------------------------------
    Return:
        info_lst (list) - list with information:
                          1) year
                          2)latitude
                          3)longtitude
                          4)path to file
    """
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument("year",\
                         help="The year in which films were made.",\
                         type=int)
    parser.add_argument("latitude",\
                         help="Latitude - part of coordinates.",\
                         type=float)
    parser.add_argument("longtitude",\
                         help="Longtitude - part of coordinates.",\
                         type=float)
    parser.add_argument("file_path",\
                         help="The path to the file with data.",\
                         type=str)
    args = parser.parse_args()

    if os.path.isfile(args.file_path): 
        path_to_file = args.file_path
    else:
        print("Error!!! This path is not the file.")

    info_lst = [args.year, args.latitude, args.longtitude, path_to_file]
    return info_lst

def creating_a_map(year, lat, lon, info_list, path_for_file):
    """
    Make the web-map file (.html).
    ----------------------------------------------------------------------------
    Arguments:
        year (int) - the year, when movies were made.
        lat (float) - latitude from user input.
        lon (float) - longtitude from user input.
        info_list (list) - the list with information:
                       1) list with coordinates of the 10 nearest places.
                       2) list with names of movies in the 10 nearest places.
                       3) list with the 10 nearest places names.
        ??? path_for_file (str) - path to file where map should be saved.
    ----------------------------------------------------------------------------
    Return nothing
    """
    import folium

    map = folium.Map(location=[lat, lon],
                     zoom_start=10,
                     tiles = "Stamen Terrain")

    html = """<h4>Location information:</h4>
    Location: {},<br>
    Film title: {}
    """


    fg_list = []
    fg = folium.FeatureGroup(name='Map of' + year)

    #[список з координатами топ10; список з назвами фільмів топ10; список з назвами локації топ10]
    #year = вказаний користувачем рік
    for coordinates_lst, name, location in info_list[0], info_list[1], info_list[2]:
        iframe = folium.IFrame(html=html.format(location, name),
                               width=300,
                               height=100)
        fg.add_child(folium.Marker(location=coordinates_lst,
                                   popup=folium.Popup(iframe),
                                   icon=folium.Icon(color = "red")))
    fg_list.append(fg)

    feature_group = folium.FeatureGroup(name='Useful information!')

    feature_group.add_child(folium.Marker(location=[49.817545, 24.023932],
                                          popup="Documents are here :-)",
                                          icon=folium.Icon()))
    fg_list.append(feature_group)

    for elem in fg_list:
        map.add_child(elem)

    map.add_child(folium.LayerControl())
    map.save('Map_name.html')

def get_coordinates(loc):
    """
    Get coordinates of location.
    """
    import geopy
    from geopy.geocoders import Nominatim

    geolocator = Nominatim(user_agent= loc)
    location = geolocator.geocode(loc)
    try:
        lat = location.latitude
        lon = location.longitude
        coordinates = (lat, lon)
    except AttributeError:
        coordinates = None

if __name__ == "__main__":
    info_lst = get_info_from_user()
    year = info_lst[0]
    lat = info_lst[1]
    lon = info_lst[2]
    path_for_file = info_lst[3]

    creating_a_map(year, lat, lon, info_list, path_for_file)

