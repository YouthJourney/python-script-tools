# -*-coding:utf-8-*-
"""
File Name: read_video.py
Program IDE: PyCharm
Create File By Author: Hong
"""
import cv2


def read_video(video_path: str):
    """
    OpenCV读视频小工具，解决视频读完报错的问题
    :param video_path: 输入需要读取的视频文件路径
    :return: 没有返回值
    """
    print('视频路径：', video_path)
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        # get a frame
        ret, frame = cap.read()
        # image to gray
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # show a frame
        if ret:
            cv2.imshow("capture", frame)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print('视频读完！')
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path = ''
    read_video(path)
