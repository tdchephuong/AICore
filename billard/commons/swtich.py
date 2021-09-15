from billard.commons.order import Order


def to_ball_name(argument):
    switcher = {
        0: "Red",
        1: "White",
        2: "Yello",
    }
    return switcher.get(argument, "nothing")

def to_order(argument):
    switcher = {
        1: Order.SECOND,
        2: Order.THIRD,
    }
    return switcher.get(argument, 0)