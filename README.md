# Movies_on_the_map

---------------------------------------------------------------------------------------------------------------------------------------------------

Призначення модуля (main.py):
Створити web-карту з 10 найближчими точок зйомок фільмів, до тієї точки, яку введе користувач.
Користувач вводить:
    1) назву модуля - main.py
    2) рік зйомки фільмів
    3) координатна широта
    4) координатна довгота
    5) шлях до бази даних (short_location.list / medium_location.list)

Інші елементи:
requirements.txt - текстовий файл з потрібними для роботи модуля бібліотеками python.
short_location.list - текстовий файл з набором інформації про фільми, роки їх зйомки, місце їх зйомки і т.д. (~1600)
medium_location.list - текстовий файл з набором інформації про фільми, роки їх зйомки, місце їх зйомки і т.д. (~5700)

Purpose of the module (main.py):
Create a web-map of the 10 nearest movie locations to the point user enters.
The user enters:
    1) module name - main.py
    2) the year of filming the movie
    3) coordinate: latitude
    4) coordinate: longitude
    5) path to the database (short_location.list / medium_location.list)

Other items:
requirements.txt - a text file with required python libraries to work with this module.
short_location.list - text file with a set of information about movies, years of their shooting, place of their shooting, etc. (~1600)
medium_location.list - text file with a set of information about movies, years of their shooting, place of their shooting, etc. (~5700)


---------------------------------------------------------------------------------------------------------------------------------------------------

Карта має 3 шари:
    1) базовий шар: "Stamen Terrain"
    2) шар з маркерами 10 наближчих точок зйомок фільмів, до тієї точки, яку введе користувач.
    3) шар з одним круглим маркером за координатами (49.817545, 24.023932)

The map has 3 layers:
    1) base layer: "Stamen Terrain"
    2) a layer with markers of 10 nearest points of shooting of films, to the point which will be entered by the user.
    3) layer with one circle marker on coordinates (49.817545, 24.023932)

---------------------------------------------------------------------------------------------------------------------------------------------------

Час роботи:
    1) short_location.list - менше хвилини.
    2) medium_location.list - ~1,5 хв.

Working time:
    1) short_location.list - less than minute.
    2) medium_location.list - ~1,5 m.

---------------------------------------------------------------------------------------------------------------------------------------------------

Приклади роботи:
Examples of module operation:

User Input:
python3 main.py 2016 49.83826 24.02324 short_location.list

