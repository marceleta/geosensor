

import math


class Mapa:
    @staticmethod
    def zoom(zoom):

        z = int(zoom)

        if z == 22:
            return 1
        elif z ==21:
            return 1
        elif z == 20:
            return 1
        elif z == 19:
            return 1
        elif z == 18:
            return 2
        elif z == 17:
            return 3
        
            