from torch._C import AnyType
from billard.models.point import Point
from billard.models.billard import to_ball_name

class Ball:

    def __init__(self, p1: Point, p2: Point, cls: int, crop: AnyType):
        self.p1 = p1
        self.p2 = p2
        self.mid_p = Ball.get_midpoint(self, p1, p2, cls)
        self.root_p = Ball.get_midpoint(self, p1, p2, 5)
        self.sum_move_x = 0
        self.sum_move_y = 0
        self.moved = False
        self.cls = cls
        self.crop = crop
        self.radius = p2.x - self.root_p.x
        self.order = 0    # order of each balls
    
    def __str__(self):
        name = to_ball_name(self.cls)
        if self.moved:
            return "---" + name + " ball has moved X: " + str(self.sum_move_x) + '\n' + name + " has moved Y: " + str(self.sum_move_y)
        return name + " ball not moving !!!"

    def get_midpoint(self, p1: Point, p2: Point, cls: int):
        if cls == 1 :
            print(" p1.y : " + str(p1.y) + " p2.y : " + str(p2.y))
            print("-- after " + str((p1.y + p2.y)/2 ))

        return Point( (p1.x + p2.x)/2 , (p1.y + p2.y)/2 )
 