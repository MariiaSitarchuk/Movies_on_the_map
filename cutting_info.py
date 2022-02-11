"""
This module was for parsering information

My first thoughts, if you're interested :-)
1) відкрити файл
2) прочитати перші 200 потрібних рядків (14 перших непотрібні)
3) взяти з них потрібну інфо
4) зробити csv файл з інфо, щоб потім читаи за допомогою pandas

[назва, рік, місце зйомок, країна]
"""

with open("locations.list", encoding="utf-8", errors='ignore') as file:
    info_list = []
    for line in file:
        film_info = line.strip().split("/t")
        #print(film_info)
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
        #print(for_loc)
        if for_loc[-1][0] != "(" and for_loc[-1][-1] != ")":
            loc = for_loc[-1]
        else:
            loc = for_loc[-2]

        loc_list = loc.split()
        country = loc_list[-1]
        
        line_lst = [name, year, loc, country]
        #print(line_lst)
        info_list.append(line_lst)

        #print("name =", name, "year =", year, "loc =", loc)

import csv
 
with open("info.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(info_list)


