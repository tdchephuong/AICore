import cv2


def detection_move():
    path_frame = "billard\\test\\Video_1"
    num1 = "60"
    num2 = "98"

    frame1_img = cv2.imread(f'{path_frame}_'+ num1 + ".jpg")
    frame2_img = cv2.imread(f'{path_frame}_'+ num2 + ".jpg")

    path_crop = "billard\\test\\crop\\Video_1"
    # crop1_img = cv2.imread(f'{path_crop}_'+ "crop_" + num1 + ".jpg")
    crop_img = cv2.imread(f'{path_crop}_'+ "crop_" + num1 + ".jpg")

    crop2_img = cv2.imread(f'{path_crop}_'+ "crop_" + num2 + ".jpg")

    res = cv2.matchTemplate(frame1_img, crop_img, 0)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print('frame : ' + '%s ' * len(min_loc) % min_loc)
    
    # res = cv2.matchTemplate(frame2_img, crop2_img, 0)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print('frame 2 : ' + '%s ' * len(min_loc) % min_loc)

def conver_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


if __name__ == '__main__':
    cv2.waitKey(3000) 
    detection_move()
