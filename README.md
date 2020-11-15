# 基于双目视觉的车辆测高系统
由双目摄像头OV9720、7寸IPS显示屏、PYNQ-z2开发平台构成，可实现车辆检测、车辆的高度、距离测量及超高检测等功能



程序结构：
measure_high 为主程序

camera_configs.py文件中保存双目摄像头标定后所需参数

my_hyperlpr.py文件为车牌识别文件

car_detection为车辆检测所需的权值文件
其中所需的文件yolov3.weights下载链接为https://github.com/jielingao/yolov3

simhei.ttf是屏幕显示的字体文件
