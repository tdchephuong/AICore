import cv2
from billard.models.ball import Ball
from billard.ultils.ultils import log_message, log_error
from billard.models.billard import to_ball_name

class Score:

    source = ""
    dict_balls = {}

    def check_exist_or_add_ball(cls: int, ball: Ball):
        if cls not in Score.dict_balls:
            Score.dict_balls[cls] = ball 
            return False
        return True

    def cal_ball_move(cls: int, next: Ball, frame: int):
        current = Score.dict_balls[cls]
        move_x, move_y = Score.cal_movement(current, next)
        if move_x > 2 :
            current.sum_move_x = move_x
            current.moved = True
        
        if move_y > 2 :
            current.sum_move_y = move_y
            current.moved = True

        if cls == 1 and (move_x > 1 or move_y > 1)  : 
            print(' --- white has moved x : ' + str(current.sum_move_x) + " y: " + str(current.sum_move_y))

    def cal_movement(current: Ball, next: Ball):
        move_x = Score.filter_motion(current.root_p.x, next.mid_p.x)
        move_y = Score.filter_motion(current.root_p.y, next.mid_p.y)

        if move_x == 1 or move_y == 1:
            return 0, 0

        return move_x, move_y
    
    def filter_motion(current: int, next: int):
        value = abs(current - next)
        return value

    def detect_motion(frame:int):
        prev_cap = cv2.VideoCapture(Score.source)
        prev_cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        _, prev = prev_cap.read()
        # cv2.imwrite(str(increment_path(imagename, mkdir=True).with_suffix('.jpg')), prev)
