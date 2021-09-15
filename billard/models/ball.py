from billard.commons.swtich import to_ball_name
from torch._C import AnyType
from billard.models.point import Point

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
            return "--- " + name + " ball has moved [X: " + str(self.sum_move_x) + ", Y: " + str(self.sum_move_y) + "]"
        return "***  " +name + " ball not moving !  ***" 
    
    def __iter__(self):
        # first start by grabbing the Class items
        iters = dict((x,y) for x,y in Ball.__dict__.items() if x[:2] != '__')

        # then update the class items with the instance items
        iters.update(self.__dict__)

        # now 'yield' through the items
        for x,y in iters.items():
            yield x,y

    def get_midpoint(self, p1: Point, p2: Point, cls: int):
        return Point( (p1.x + p2.x)/2 , (p1.y + p2.y)/2 )
 