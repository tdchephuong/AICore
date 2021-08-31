
def to_ball_name(argument):
    switcher = {
        0: "Red",
        1: "White",
        2: "Yello",
    }
    return switcher.get(argument, "nothing")