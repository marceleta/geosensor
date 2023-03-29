from shapely.geometry import Polygon, Point
import json

class Geometry:

    @staticmethod
    def pontos_na_area(polygon, posicoes):
        polygon = json.loads(polygon)
        pontos = []
        for ponto in polygon:
            p = ponto['lat'], ponto['lng']
            pontos.append(p)

        polygon = Polygon(pontos)
        contains = []
        for posicao in posicoes:
            point = Point(posicao.to_tuple())
            if polygon.contains(point):
                contains.append(posicao.to_dict())
        
        return contains
            