import math
from billard.commons.swtich import to_order, to_ball_name
from billard.commons.order import Order
import cv2
from billard.models.ball import Ball
from billard.ultils.ultils import log_message, log_error

class Score:

    source = ""
    dict_balls = {}
    calc_correl = False
    first_ball = None
    third_ball = None
    
    frame_third_ball_corel = 0
    distance_first_third = 0

    def check_exist_or_add_ball(cls: int, ball: Ball):
        if cls not in Score.dict_balls:
            Score.dict_balls[cls] = ball 
            return False
        return True

    def cal_correlation(frame: int):
        if Score.first_ball is None:
            Score.first_ball = Score.get_ball_by_ord(Order.FIRST)

        if Score.third_ball is None:
            Score.third_ball = Score.get_ball_by_ord(Order.THIRD)

        distance = math.sqrt( (Score.third_ball.mid_p.x - Score.first_ball.mid_p.x)**2 + (Score.third_ball.mid_p.y - Score.first_ball.mid_p.y)**2 ) 
        
        if distance < Score.distance_first_third:
            Score.distance_first_third = distance
            Score.frame_third_ball_corel = frame

    def cal_ball_move(cls: int, next: Ball, frame: int):
        current = Score.dict_balls[cls]
        move_x, move_y = Score.cal_movement(current, next)
        if move_x > 2 :
            current.sum_move_x = move_x
            current.moved = True
        
        if move_y > 2 :
            current.sum_move_y = move_y
            current.moved = True

        if current.order == 0 and current.moved:
            order = Score.get_order()
            if order == Order.THIRD:
                Score.calc_correl = True
                current.frame_moving = frame

            current.order = order
        

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

    def get_order():
        order = 0
        for k, v in Score.dict_balls.items():
            data = to_order(int(v.order))
            if data != 0 :
                order = data

        if order == 0:
            return Order.FIRST
        return order

    # def set_third_ball():
    #     for k, v in Score.dict_balls.items():
    #         if int(v.order) == 0:
    #             v.order = Order.THIRD
    #             break
    
    def get_ball_by_ord(order):
        for k, v in Score.dict_balls.items():
            if v.order == order:
                return v
        