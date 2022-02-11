# Movies_on_the_map

(цей модуль ще не завершений)
(this module is not finished)

---------------------------------------------------------------------------------------------------------------------------------------------------

Призначення модуля (main.py):
Створити web-карту з 10 найближчими точок зйомок фільмів, до тієї точки, яку введе користувач.
Користувач вводить:
    1) назву модуля - main.py
    2) рік зйомки фільмів
    3) координатна широта
    4) координатна довгота
    5) шлях до бази даних (short_info.csv)

Інші елементи:
requirements.txt - текстовий файл з потрібними для роботи модуля бібліотеками python.
short_location.list - текстовий файл з набором інйормації про фільми, роки їх зйомки, місце їх зйомки і т.д.
short_info.csv - новостворений csv-файл з відібраною інформацією з файлу short_location.list.
cutting_info.py - програма, що відбирає потрібну інформацію з файлу short_location.list та записує її в новий файл short_info.csv.

Purpose of the module (main.py):
Create a web-map of the 10 nearest movie locations to the point user enters.
The user enters:
    1) module name - main.py
    2) the year of filming the movie
    3) coordinate: latitude
    4) coordinate: longitude
    5) path to the database (short_info.csv)

Other items:
requirements.txt - a text file with required python libraries to work with this module.
short_location.list - text file with a set of information about movies, years of their shooting, place of their shooting, etc.
short_info.csv - newly created csv file with information displayed from the short_location.list file.
cutting_info.py - a program that extracts the necessary information from the file short_location.list and writes it to a new file short_info.csv.

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

Приклади роботи:
Examples of module operation:

(ще не додано)
(not yet added)