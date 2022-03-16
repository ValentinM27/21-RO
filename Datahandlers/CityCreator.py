import random

from Objects.City import City
from copy import copy
import math


# Classe permettant d'initialiser une liste de villes grâce à un fichier txt
# et de la stocker
class CityCreator:
    """
    Permet de créer un objet de type CityCreator
    """

    def __init__(self, filename):
        self.listcity = []
        self.filename = filename
        self._init_list()

    '''
    Permet d'initialiser une liste de ville
    '''

    def _init_list(self):

        with open(self.filename) as file:
            lines = file.readlines()

            for line in lines:
                line = line.split(" ")
                self.listcity.append(City(line[0], line[1], line[2], line[3]))

    '''
    Permet de lister les villes de la liste
    '''

    def _list_city(self):
        for city in self.listcity:
            print(city.idcity + " " + city.name)

    '''
    Permet de calculer la distance entre deux villes
    '''

    def _distance_city(self, city1, city2):
        y1 = city1.getY()
        y2 = city2.getY()

        x1 = city1.getX()
        x2 = city2.getX()

        distance = abs(
            6371 * math.acos((math.sin(y1) * math.sin(y2)) + (math.cos(y1) * math.cos(y2) * math.cos(x1 - x2))))
        return distance

    '''
    Permet d'effectuer une tournée dans le sens croissant avec les distance parcouru
    '''

    def _ordered_tour(self):
        ordered_tour = []

        for city in self.listcity:
            ordered_tour.append(city)

        return ordered_tour

    '''
    Permet d'afficher une liste tour
    '''

    def affichertour(self, tour):
        listtour = []

        for city in tour:
            listtour.append(int(city.idcity))

        print(listtour)

    '''
    Permet de calculer la distance parcouru dans une tournée
    '''

    def cout(self, tour):
        distance = 0

        i = 1
        for i in range(len(tour)):
            distance += self._distance_city(tour[i], tour[i - 1])

        return distance

    '''
    Permet d'effectuer un parcour aléatoire
    '''

    def _tour_aleatoire(self, listcity):
        return list(random.sample(listcity, len(listcity)))

    '''
    Permet de trouver le la distance minimal par plus proche voisin pour aller
    à une ville en paramètre depuis Dijon
    '''

    def plus_proche_voisin(self, city1):
        t1 = [city1]
        list_city = copy(self.listcity)

        while len(list_city) > 1:
            next_ = self.plus_proche(city1, list_city)
            t1.append(next_)
            city1 = next_

        return t1

    '''
    Permet de trouver la vile la plus proche d'une autre
    '''

    def plus_proche(self, city1, listcity):
        if city1 in listcity:
            listcity.pop(listcity.index(city1))

        min_dist = 0
        closest_city = None

        for city in listcity:
            new_distance = self._distance_city(city, city1)

            if min_dist != 0:
                if min_dist > new_distance:
                    min_dist = new_distance
                    closest_city = city
            else:
                closest_city = city
                min_dist = new_distance

        return closest_city

    '''
    Permet de trouver une tournée gloutone via le plus proche voisin amélioré
    '''

    def plus_proche_voisin_ameliore(self):
        best_tour = []
        best_distance = 0

        for city in self.listcity:
            new_t = self.plus_proche_voisin(city)
            new_dist = self.cout(new_t)

            if best_distance != 0:
                if best_distance > new_dist:
                    best_tour = new_t
                    best_distance = new_dist
            else:
                best_tour = new_t
                best_distance = new_dist

        return best_tour

    '''
    Permet de déterminer les deux ville les éloignées
    '''

    def plus_loin(self):
        max_dist = 0
        city1, city2 = None, None

        for c1 in self.listcity:
            for c2 in self.listcity:
                new_distance = self._distance_city(c1, c2)

                if max_dist != 0 and new_distance > 0:
                    if max_dist < new_distance:
                        max_dist = new_distance
                        city1, city2 = c1, c2
                elif new_distance > 0:
                    max_dist = new_distance
                    city1, city2 = c1, c2

        return city1, city2, max_dist

    '''
    Permet de trouver une tournée gloutone par insertion proche
    '''

    def insertion_proche(self):
        listcity = copy(self.listcity)
        city1, city2, _ = self.plus_loin()

        if city1 and city2 in listcity:
            listcity.pop(listcity.index(city1))
            listcity.pop(listcity.index(city2))

        t2 = [city1, city2]

        # On visite toutes les villes une à une
        for city in listcity:
            shortest_tour = None
            shortest_distance = None

            # On teste toutes les posibilité de nouvelles tournées par insertion
            for element in t2:
                new_tour = copy(t2)
                new_tour.insert(new_tour.index(element), city)
                new_distance = self.cout(new_tour)

                if shortest_tour is not None and shortest_distance is not None:
                    if shortest_distance > new_distance:
                        shortest_tour = new_tour
                        shortest_distance = new_distance
                else:
                    shortest_tour = new_tour
                    shortest_distance = new_distance

            # On retiens la tournée la plus courte trouvée actuellement
            t2 = shortest_tour

        return t2

    '''
    Permet de trouver une tournée gloutone par insertion loin 
    '''

    def insertion_loin(self):
        listcity = copy(self.listcity)
        city1, city2, _ = self.plus_loin()

        t2 = [city1, city2]

        if city1 and city2 in listcity:
            listcity.pop(listcity.index(city1))
            listcity.pop(listcity.index(city2))

        for city in listcity:
            longest_tour = None
            longest_distance = None

            for element in t2:
                new_tour = copy(t2)
                new_tour.insert(new_tour.index(element), city)
                new_distance = self.cout(new_tour)

                if longest_tour is not None and longest_distance is not None:
                    if longest_distance < new_distance:
                        longest_tour = new_tour
                        longest_distance = new_distance
                else:
                    longest_tour = new_tour
                    longest_distance = new_distance

            t2 = longest_tour

        return t2

    '''
    Permet d'effectuer une rechercher locale
    '''

    def recherche_locale(self, t_entree):
        t_courante = copy(t_entree)
        fini = False

        while not fini:
            fini = True
            n = len(t_courante)

            for i in range(len(t_courante)):
                d1 = self._distance_city(t_courante[(i - 1) % n], t_courante[i]) + self._distance_city(
                    t_courante[(i + 1) % n], t_courante[(i + 2) % n])
                d2 = self._distance_city(t_courante[(i - 1) % n], t_courante[(i + 1) % n]) + self._distance_city(
                    t_courante[i], t_courante[(i + 2) % n])

                if d1 > d2:
                    t_courante[i], t_courante[i + 1] = t_courante[i + 1], t_courante[i]
                    fini = False

        return t_courante

    '''
    Permet d'effectuer une rechercher locale
    '''
    def recherche_local_ij_premier(self, t_entree):
        t_courante = copy(t_entree)
        fini = False

        while not fini:
            fini = True

            for i in range(len(t_courante)):
                for j in range(i + 1, len(t_courante)):

                    d = self.cout(t_courante)
                    t_courante[i], t_courante[j] = t_courante[j], t_courante[i]

                    if d < self.cout(t_courante):
                        t_courante[i], t_courante[j] = t_courante[j], t_courante[i]
                    else:
                        fini = False

        return t_courante
