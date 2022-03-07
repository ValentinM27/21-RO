import math

"""
Classe gérant la structure d'une ville
"""

class City:
    """
    Constructeur la classe City, permet d'instancier un objet city
    """

    def __init__(self, idcity, name, latitude, longitude):
        self.idcity = idcity
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def getX(self):
        return math.radians(float(self.longitude))

    def getY(self):
        return math.radians(float(self.latitude))

    def getName(self):
        return self.name

    def getID(self):
        return self.idcity
