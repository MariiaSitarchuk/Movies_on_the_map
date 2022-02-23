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
                          2) latitude
                          3) longtitude
                          4) path to file
                          5) country
    ---------------------------------------------------
    >>> python main.py 2000 49.83826 24.02324 short_location.list
    [2000, 49.83826, 24.02324, short_location.list, 'Ukraine']
    """
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument("year",\
                         help="The year in which films were made.",\
                         type=int)
    parser.add_argument("latitude",\
                         help="Latitude - part of coordinates.",\
                         type=str)
    parser.add_argument("longtitude",\
                         help="Longtitude - part of coordinates.",\
                         type=str)
    parser.add_argument("file_path",\
                         help="The path to the file with data.",\
                         type=str)
    args = parser.parse_args()

    if os.path.isfile(args.file_path): 
        path_to_file = args.file_path
    else:
        print("Error!!! This path is not the file.")

    info_lst = [args.year, args.latitude, args.longtitude, path_to_file]

    from geopy.geocoders import Nominatim

    geolocator = Nominatim(user_agent="myGeolocator")
    coordinates = str(info_lst[1] + ", " + info_lst[2])
    location = geolocator.reverse(coordinates)
    all_address_dict = location.raw['address']
    country = all_address_dict.get['country']
    if country == 'United States of America':
        country = 'USA'
    elif country == 'United Kingdom':
        country = 'UK'

    info_lst.append(country)

    return info_lst

def creating_a_map(year, lat, lon, info_list):
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
    ----------------------------------------------------------------------------
    Return:
        nothing, but creates a html file with a map.
    ----------------------------------------------------------------------------
    >>> creating_a_map(2000, 49.83826, 24.02324, info_list)
    
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
    fg = folium.FeatureGroup(name='Map of ' + str(year))

    #[список з координатами топ10; список з назвами фільмів топ10; список з назвами локації топ10]
    #year = вказаний користувачем рік
    for coordinates_lst, name, location in info_list[0], info_list[1], info_list[2]:
        #coordinates_lst - [lat, lon]
        # name - 'Title'
        # location - 'Street, city, country'
        iframe = folium.IFrame(html=html.format(location, name),
                               width=300,
                               height=100)
        fg.add_child(folium.Marker(location=coordinates_lst,
                                   popup=folium.Popup(iframe),
                                   icon=folium.Icon(color = "red")))
    fg_list.append(fg)

    feature_group = folium.FeatureGroup(name='Useful information!')

    feature_group.add_child(folium.CircleMarker(location=[49.817545, 24.023932],
                                                 radius=10,
                                                 popup="Documents are here :-)",
                                                 fill_color='red',
                                                 color='red',
                                                 fill_opacity=0.5))

    fg_list.append(feature_group)

    for elem in fg_list:
        map.add_child(elem)

    map.add_child(folium.LayerControl())
    map.save('Map_name.html')

def get_coordinates():
    """
    Creates DataFrame by deleting duplicates from usual DataFrame 
    (from file with cutted information).
    Get coordinates of every (unique) location.
    Add new colum with coordinates to DataFrame.
    -----------------------------------------------------------------
    Argument:
        no arguments needed.
    -----------------------------------------------------------------
    Return:
        without_dupl - DataFrame without duplicates
                       and with coordinates colum.
    -----------------------------------------------------------------
    """
    import pandas as pd
    import geopy
    from geopy.geocoders import Nominatim
    # from geopy.extra.rate_limiter import RateLimiter

    df = pd.read_csv("cutted_info.csv")
    without_dupl = df.drop_duplicates(subset=["name", "loc"])
    coordinates_lst = []

    """
    OR:

    geolocator = Nominatim(user_agent= 'Something')
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    without_dupl['loc_data'] = without_dupl['loc'].apply(geocode)
    without_dupl['Lat'] = without_dupl['loc_data'].apply(lambda x: x.latitude if x else None)
    without_dupl['Lon'] = without_dupl['loc_data'].apply(lambda x: x.longitude if x else None)
    without_dupl.drop(columns = ['loc_data'],axis = 1, inplace = True)
    """

    for _, data_loc in without_dupl.iterrows():
        loc_info = data_loc['loc']
        geolocator = Nominatim(user_agent= 'Something')
        location = geolocator.geocode(loc_info)
        try:
            lat = location.latitude
            lon = location.longitude
            coordinates = [float(lat), float(lon)]
        except AttributeError:
            coordinates = None
        coordinates_lst.append(coordinates)

    without_dupl.insert(loc=-1, column="coordinates", value=coordinates_lst)

    return without_dupl

def find_nearest(data_frame, user_lat, user_lon):
    """
    Find distance between user point and coordinates of filming location.
    Make a new colum in DataFrame - "dist".
    Make a list of 10 nearest places.
    -----------------------------------------------------------------------
    Argument:
        data_frame - cutted DataFrame with coordinates.
        user_lat (float) - user's latitude.
        user_lon (float) - user's longtitude.
    -----------------------------------------------------------------------
    Return:
        the_lst (list) - list with information (about the 10 nearest places),
                  which will be used to create the map.
    the_lst = [ [coordinates1, coordinates2 ... coordinates10],\
                [name1, name2 ... name10], [loc1, loc2 ... loc10] ]
    """
    def find_distance(place_coor, lat, lon):
        """
        Find distance between user point and point of filming location.
        ------------------------------------------------------------------------
        Aarguments:
            place_coor (list) - [latitude, longtitude], of a filming location.
            lat (float) - user's latitude.
            lon (float) - user's longtitude.
        ------------------------------------------------------------------------
        Return:
            dist (float) - the distance between those two points.
        ------------------------------------------------------------------------
        >>> lat = 53.4235217000000020
        >>> lon = -113.4741271000000040
        >>> place_coor = [53.5343457999999970, -113.5013688000000229]
        >>> find_distance(place_coor, lat, lon)
        12.466096663282977
        """
        from geopy import distance
        user_coor = (lat, lon)
        film_coor = tuple(place_coor)
        dist = distance.distance(user_coor, film_coor).kilometers
        return dist
    
    dist_lst = []

    for _, row in data_frame.iterrows():
        if row["coordinates"] != None:
            distance = find_distance(row["coordinates"], user_lat, user_lon)
        else:
            distance = None
        dist_lst.append(distance)

    data_frame.insert(loc=-1, column="dist", value=dist_lst)

    #---------------------------------------------------------------------------------------------
    import pandas as pd

    the_lst = []
    name_lst = []
    loc_lst = []
    coor_lst = []

    for _ in range(10):
        for _, row in data_frame.iterrows():
            if row["dist"] == data_frame.dist.min():
                name_lst.append(row["name"])
                loc_lst.append(row["loc"])
                coor_lst.append(row["coordinates"])
        data_frame.loc[(data_frame.dist == data_frame.dist.min()), 'dist'] = None
    the_lst.append(coor_lst, name_lst, loc_lst)

    return the_lst


def cutting_info(path_of_file, user_country, user_year):
    """
    Cuts information in file with data.
    -------------------------------------------------------------
    Argument:
        path_of_file (str) - the path to file with data.
        user_country (str) - the country, in which 
                             user is searching movies.
        user_year (int) - the year, in which 
                          user is searching movies.
    -------------------------------------------------------------
    Return:
        nothing, but creates a csv file with cutted information.
    -------------------------------------------------------------
    >>> cutting_info(short_location.list, 'USA', 2014)

    >>> cutting_info(locations.list, 'Canada', 2016)

    """
    with open(path_of_file, encoding="utf-8", errors='ignore') as file:
        info_list = []
        for line in file:
            film_info = line.strip().split("/t")
            film = film_info[0].split()[:-1]
            for elem in film:
                if elem[0] == "(" and elem[-1] == ")":
                    try:
                        year = int(elem[1:-1])
                        year_index = film.index(elem)
                        break
                    except ValueError:
                        do ="nothing"
            name_lst = film[:year_index]
            name = " ".join(name_lst)

            for_loc = line.strip().split("\t")

            if for_loc[-1][0] != "(" and for_loc[-1][-1] != ")":
                loc = for_loc[-1]
            else:
                loc = for_loc[-2]

            loc_list = loc.split()
            country = loc_list[-1]

            if year == user_year and country == user_country:
                line_lst = [name, year, loc, country]
                info_list.append(line_lst)
            else:
                do = "absolutely nothing"

    info_list.insert(0, ["name", "year", "loc", "country"])

    import csv
 
    with open("cutted_info.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(info_list)

if __name__ == "__main__":
    """
    info_lst = get_info_from_user()

    year = info_lst[0]
    lat = float(info_lst[1])
    lon = float(info_lst[2])
    path_of_file = info_lst[3]
    country = info_lst[4]

    cutting_info(path_of_file, country, year)

    data_frame_with_coordinates = get_coordinates()

    info_list = find_nearest(data_frame_with_coordinates, lat, lon)

    creating_a_map(year, lat, lon, info_list)
    """

    import doctest
    doctest.testmod()


"""
def custom_geocoder(address):
        import geopy
        from geopy.geocoders import Nominatim
        from geopandas.tools import geocode

        dataframe = geocode(address , provider="nominatim" , user_agent = 'my_request') 
        point = dataframe.geometry.iloc[0] 
        return pd.Series({'Latitude': point.y, 'Longitude': point.x}) 
        #Applying function to the dataframe 
        #a_dataframe.insert(loc=1, column="B", value=[4, 5, 6])

without_dupl[['latitude' , 'longitude']] = without_dupl.loc.apply( lambda x: custom_geocoder(x))
"""
