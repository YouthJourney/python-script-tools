# -*-coding:utf-8-*-
"""
File Name: read_video.py
Program IDE: PyCharm
Create File By Author: Hong
"""
import cv2


def image_to_video(first_img_path: str, img_base_folder: str, video_name: str, img_shape: tuple, fps: int,
                   img_count: int, is_default_shape=False):
    """
    图片生成小工具
    主要是将一个目录下的所有图片合成
    :param first_img_path: 第一张图片的路径
    :param img_base_folder: 图片所在目录
    :param video_name: 生成的视频名称
    :param img_shape: 确定视频每一帧形状
    :param fps: 视频帧
    :param img_count:目录中的数量
    :param is_default_shape: 是否使用图片的形状
    :return: 没有返回值
    """
    # 获取一张图片的宽高作为视频的宽高
    if not is_default_shape:
        image = cv2.imread(first_img_path)
        # cv2.imshow("new window", image)  # 显示图片
        image_info = image.shape
        print(image_info)
        height = image_info[0]
        width = image_info[1]
        size = (height, width)
        print(size)

    else:
        size = img_shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(video_name, fourcc, fps, size)  # 创建视频流对象-格式一

    """
    参数1 即将保存的文件路径
    参数2 VideoWriter_fourcc为视频编解码器
        fourcc意为四字符代码（Four-Character Codes），顾名思义，该编码由四个字符组成,下面是VideoWriter_fourcc对象一些常用的参数,注意：字符顺序不能弄混
        cv2.VideoWriter_fourcc('I', '4', '2', '0'),该参数是YUV编码类型，文件名后缀为.avi 
        cv2.VideoWriter_fourcc('P', 'I', 'M', 'I'),该参数是MPEG-1编码类型，文件名后缀为.avi 
        cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),该参数是MPEG-4编码类型，文件名后缀为.avi 
        cv2.VideoWriter_fourcc('T', 'H', 'E', 'O'),该参数是Ogg Vorbis,文件名后缀为.ogv 
        cv2.VideoWriter_fourcc('F', 'L', 'V', '1'),该参数是Flash视频，文件名后缀为.flv
        cv2.VideoWriter_fourcc('m', 'p', '4', 'v')    文件名后缀为.mp4
    参数3 为帧播放速率
    参数4 (width, height)为视频帧大小
    """
    for i in range(1, img_count + 1):
        file_name = img_base_folder + '/' + str(i) + '.jpg'
        image = cv2.imread(file_name)
        video.write(image)  # 向视频文件写入一帧--只有图像，没有声音

    print('视频生成完成')


if __name__ == '__main__':
    first_img_path = 'fps/fps10000.jpg'
    img_base_folder = 'fps'
    video_name = 'result.mp4'
    img_shape = (640, 640)
    fps = 30
    img_count = 136
    image_to_video(first_img_path, img_base_folder, video_name, img_shape, fps, img_count)
