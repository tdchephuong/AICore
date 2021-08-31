
from billard.models.ball import Ball
from billard.ultils.ultils import log_message, log_error
from billard.models.billard import to_ball_name

class Score:
    
    filter = 3
    dict_balls = {}

    def check_exist_or_add_ball(cls: int, ball: Ball):
        if cls not in Score.dict_balls:
            Score.dict_balls[cls] = ball 
            return False
        return True

    def cal_ball_move(cls: int, ball: Ball):
        current = Score.dict_balls[cls]
        move = Score.cal_movement(current, ball)
        name = to_ball_name(cls)
        log_message( name + " has moved: " + str(move))
        current.move = move

    def cal_movement(current: Ball, next: Ball):
        move = 0
        move += Score.filter_motion(current.midpoint.x, next.midpoint.x)
        move += Score.filter_motion(current.midpoint.y, next.midpoint.y)
        return move
    
    def filter_motion(current: int, next: int):
        value = abs(current - next)
        if(value > Score.filter) :
            return value
        return 0

    
 
