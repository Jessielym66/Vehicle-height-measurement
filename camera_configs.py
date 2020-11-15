import cv2
import numpy as np

left_camera_matrix = np.array([[656.55552, 0., 329.22675],
                               [0., 655.55451, 233.84735],
                               [0., 0., 1.]])
left_distortion = np.array([[0.20312, -0.75655, 0.00109, 0.00839, 0.00000]])



right_camera_matrix = np.array([[663.67937, 0., 331.95201],
                                [0., 660.76637, 185.16237],
                                [0., 0., 1.]])
right_distortion = np.array([[0.20108, -0.64528, -0.00294, 0.00892, 0.00000]])


R = np.matrix([
    [ 1.00000,    0.00064,   -0.00270],
    [-0.00067,    0.99993,    0.01098],
    [ 0.00270,   -0.01098,    0.99993],
])
 # 旋转关系向量

T = np.array([-121.63300, 0.40579, 0.19973]) # 平移关系向量

size = (640, 480) # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)