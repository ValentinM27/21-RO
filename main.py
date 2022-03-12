from Datahandlers.CityCreator import CityCreator
from copy import copy

# Classe main du programme
if __name__ == '__main__':
    CityCreator = CityCreator('top80.txt')
    # CityCreator._list_city()
    distance = CityCreator._distance_city(CityCreator.listcity[0], CityCreator.listcity[1])

    print(
        "La distance entre " + CityCreator.listcity[0].name + " et " + CityCreator.listcity[1].name + " est de " + str(
            distance) + " km")

    ordered_tour = CityCreator._ordered_tour()

    print("Tournée croissante")
    CityCreator.affichertour(ordered_tour)
    print("La distance lors de la tournée est de : " + str("{:.2f}".format(CityCreator.cout(ordered_tour))) + " km")

    print("-------------------")
    listcity = CityCreator.listcity
    random_tour = CityCreator._tour_aleatoire(listcity)
    print("Tournée aléatoire")
    CityCreator.affichertour(random_tour)
    print("La distance lors de la tournée aléatoire est de : " + str(
        "{:.2F}".format(CityCreator.cout(random_tour))) + " km")

    print("-------------------")
    copyList = copy(CityCreator.listcity)
    print(f"Ville la plus proche de {CityCreator.listcity[0].getName()} : {CityCreator.plus_proche(CityCreator.listcity[0], copyList).getName()}")

    glouton_proche = CityCreator.plus_proche_voisin(CityCreator.listcity[0])

    print("Tournée gloutone plus proche voisin : ")
    CityCreator.affichertour(glouton_proche)

    print("La distance lors de la tournée glouton par plus proche voisin est de : " + str(
        "{:.2F}".format(CityCreator.cout(glouton_proche))) + " km")

    print("-------------------")
    glouton_proche = CityCreator.plus_proche_voisin_ameliore()
    print("Tournée gloutone plus proche voisin amélioré : ")
    CityCreator.affichertour(glouton_proche)

    print("La distance lors de la tournée glouton par plus proche voisin amélioré est de : " + str(
        "{:.2F}".format(CityCreator.cout(glouton_proche))) + " km")

    print("-------------------")
    city1, city2, distance = CityCreator.plus_loin()

    print(f"Les villes les plus éloignées sont {city1.getName(), city1.getID()} et {city2.getName(), city2.getID()}"
          f" et elle le sont " +
          str("{:.2f}".format(distance)) + " km")

    copyList = copy(CityCreator.listcity)

    glouton_insertion = CityCreator.insertion_proche()
    print("Tournée gloutone par insertion : ")
    CityCreator.affichertour(glouton_insertion)

    print("La distance lors de la tournée glouton par insertion amélioré est de : " + str(
        "{:.2F}".format(CityCreator.cout(glouton_insertion))) + " km")

    print(len(glouton_insertion))

    print("-------------------")

    copyList = copy(CityCreator.listcity)

    glouton_insertion = CityCreator.insertion_loin()
    print("Tournée gloutone par insertion loin: ")
    CityCreator.affichertour(glouton_insertion)

    print("La distance lors de la tournée glouton par insertion loin est de : " + str(
        "{:.2F}".format(CityCreator.cout(glouton_insertion))) + " km")