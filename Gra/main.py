from edge import Edge
from hexagon import Hexagon
from point import Point
from random import choice
from player import Player

p_amount = int(input("Ilu jest graczy? "))
players_list = []
for i in range(p_amount):
    players_list.append(Player(input("Podaj nazwę " + str(i + 1) + ". gracza:")))
print("Gracze: ")
for i in range(players_list.__len__()):
    print(players_list[i].name)

hex_list = []
edge_list = []
point_list = []
number_list = []
resource_list = []
# czytanie pliku
file = open("mapa.txt")
size = file.readline()
size = size.split(" ")
rows = int(size[0])
columns = int(size[1])
map_design = file.read()
file.close()
map_design = map_design.replace("\n", "").replace(" ", "")
# wypełnianie hex_list
for i in range(map_design.__len__()):
    if map_design[i] == "w":
        hex_list.append(Hexagon("water", None, None))
    elif map_design[i] == "l":
        if number_list.__len__() == 0:
            number_list.extend([2, 3, 4, 5, 6, 8, 9, 10, 11, 12])
        if resource_list.__len__() == 0:
            resource_list.extend(["bricks", "grain", "lumber", "ore", "wool"])
        tmp_number = choice(number_list)
        number_list.remove(tmp_number)
        tmp_resource = choice(resource_list)
        resource_list.remove(tmp_resource)
        hex_list.append(Hexagon("land", tmp_number, tmp_resource))
    elif map_design[i] == "p":
        hex_list.append(Hexagon("sand", None, None))
# wypełnianie edge_list[].hexes i edge_list[].points i point_list[].hexes
for id in range(columns * (rows - 1)):
    if id % (2 * columns) < columns:  # hexy przesunięte w prawo
        if id % columns != columns - 1:  # mają hexy po prawej
            if id % columns != 0:  # mają hexy po lewej
                edge_list.append(Edge([id, id + columns]))  # krawędź lewa dolna
                edge_list[edge_list.__len__() - 1].add_points([point_list.__len__() - 1, point_list.__len__()])  # krawędź lewa dolna ma wierzchołek lewy dolny i dolny
            edge_list.append(Edge([id, id + columns + 1]))  # krawędź prawa dolna
            point_list.append(Point([id, id + columns, id + columns + 1]))  # wierzchołek dolny
            point_list.append(Point([id, id + 1, id + columns + 1]))  # wierzchołek prawy dolny
            edge_list[edge_list.__len__() - 1].add_points([point_list.__len__() - 2, point_list.__len__() - 1])  # krawędź prawa dolna ma wierzchołek dolny i prawy dolny
            if id > columns - 1:  # mają hexy z góry
                edge_list.append(Edge([id, id + 1]))  # krawędź prawa
                edge_list[edge_list.__len__() - 1].add_points([point_list.__len__() - 2 * columns + 1, point_list.__len__() - 1])  # krawędź prawa ma wierzchołek prawy górny i prawy dolny
    else:  # hexy przesunięte w lewo
        if id % columns != 0:  # mają hexy po lewej
            edge_list.append(Edge([id, id + columns - 1]))  # krawędź lewa dolna
            point_list.append(Point([id, id + columns - 1, id + columns]))  # wierzchołek dolny
            edge_list[edge_list.__len__() - 1].add_points([point_list.__len__() - 2, point_list.__len__() - 1])  # krawędź lewa dolna dostaje wierzchołek lewy dolny i dolny
        if id % columns != columns - 1:  # mają hexy po prawej
            if id % columns != 0:  # mają hexy po lewej
                edge_list.append(Edge([id, id + columns]))  # krawędź prawa dolna
                edge_list[edge_list.__len__() - 1].add_points([point_list.__len__() - 1, point_list.__len__()])  # krawędź prawa dolna dostaje wierzchołek dolny i prawy dolny
            point_list.append(Point([id, id + 1, id + columns]))  # wierzchołek prawy dolny
            edge_list.append(Edge([id, id + 1]))  # krawędź prawa
            edge_list[edge_list.__len__() - 1].add_points([point_list.__len__() - 2 * columns + 1, point_list.__len__() - 1])  # krawędź prawa dostaje wierzchołek prawy górny i prawy dolny

# wypełnianie point_list[].edges
tmp_edges = []
for i in range(point_list.__len__()):
    for j in range(edge_list.__len__()):
        tmp_edges.append([])
        if i in edge_list[j].points:
            tmp_edges[i].append(j)
    point_list[i].add_edges(tmp_edges[i])

# wypełnianie point_list[].points
tmp_points = []
for i in range(point_list.__len__()):
    tmp_points.append([])
    for j in range(point_list[i].edges.__len__()):
        for k in range(edge_list[point_list[i].edges[j]].points.__len__()):
            if edge_list[point_list[i].edges[j]].points[k] != i:
                tmp_points[i].append(edge_list[point_list[i].edges[j]].points[k])
    point_list[i].points = tmp_points[i]

#wypełnianie edge_list[].edges
tmp_edges.clear()
for i in range(edge_list.__len__()):
    tmp_edges.append([])
    for j in range(edge_list[i].points.__len__()):
        for k in range(point_list[edge_list[i].points[j]].edges.__len__()):
            if point_list[edge_list[i].points[j]].edges[k] != i:
                tmp_edges[i].append(point_list[edge_list[i].points[j]].edges[k])
    edge_list[i].edges = tmp_edges[i]

print("Lista sześcianów z surowcami:")
for i in range(hex_list.__len__()):
    if hex_list[i].type == "land":
        print(i, "[", hex_list[i].number, hex_list[i].resource + "]")

print("Lista krawędzi:")
for i in range(edge_list.__len__()):
    print(i, "ID sześcianów: ", edge_list[i].hexes, "ID wierzchołków: ", edge_list[i].points, "ID krawędzi :", edge_list[i].edges)

print("Lista wierzchołków:")
for i in range(point_list.__len__()):
    print(i, "ID sześcianów: ", point_list[i].hexes, "ID krawędzi: ", point_list[i].edges, "ID wierzchołków :", point_list[i].points)

# start gry
i = 0
free_point_id_list = []
free_edges_id_list = []
for i in range(point_list.__len__()):
    is_land = 0
    for j in range(point_list[i].hexes.__len__()):
        if hex_list[point_list[i].hexes[j]].type == "land":
            is_land = 1
    if is_land == 1:
        free_point_id_list.append(i)
for i in range(edge_list.__len__()):
    is_land = 0
    for j in range(edge_list[i].hexes.__len__()):
        if hex_list[edge_list[i].hexes[j]].type == "land":
            is_land = 1
    if is_land == 1:
        free_edges_id_list.append(i)
j = 0
while j < 2*players_list.__len__():
    if j<players_list.__len__():
        i = j
    else:
        i = 2*players_list.__len__() - 1 - j
    print("Ruch " + str(j) + ", gra " + players_list[i].name)
    print("Dostępne wierzchołki to:")
    print(free_point_id_list)
    choice = int(input("Wybierz wierzchołek: "))
    free_point_id_list.remove(choice)
    for k in range(point_list[choice].points.__len__()):
        if point_list[choice].points[k] in free_point_id_list:
            free_point_id_list.remove(point_list[choice].points[k])
    point_list[choice].player = players_list[i].name
    point_list[choice].settlement = 1
    players_list[i].settlements.append(choice)
    players_list[i].settlements_left -= 1

    if j >= players_list.__len__():
        hex_list[choice].return_resource(players_list[i])
    print("Dostępne drogi to:")
    for k in range(point_list[choice].edges.__len__()):
        if point_list[choice].edges[k] in free_edges_id_list:
            print(point_list[choice].edges[k])
    choice = int(input("Wybierz krawędź dla swojej drogi: "))
    free_edges_id_list.remove(choice)
    edge_list[choice].player = players_list[i].name
    edge_list[choice].road = 1
    players_list[i].roads.append(choice)
    players_list[i].long_road += 1
    players_list[i].roads_left -= 1

    j += 1
