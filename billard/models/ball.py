from billard.models.point import Point
from billard.models.billard import to_ball_name

class Ball:

    def __init__(self, p1: Point, p2: Point, cls: int):
        self.p1 = p1
        self.p2 = p2
        self.midpoint = Point( (p1.x +p2.x)/2, (p1.y + p2.y)/2 )
        self.move = 0
        self.cls = cls
        self.width = p2.x - self.midpoint.x
    
    def __str__(self):
        name = to_ball_name(self.cls)
        return name + " has moved: " + str(self.move)

    def get_midpoint(self, p1: Point, p2: Point):
        return Point( (p1.x +p2.x)/2, (p1.y + p2.y)/2 )
 