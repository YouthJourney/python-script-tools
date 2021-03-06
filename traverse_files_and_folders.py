# -*-coding:utf-8-*-
"""
File Name: read_video.py
Program IDE: PyCharm
Create File By Author: Hong
"""
import os
import shutil


def move_files_to_new_folder(old_base_folder: str, new_folder: str, file_type: str, is_rename=True):
    """
    一个移动根目录下的所有目录下的文件到新的文件下的小工具
    主要功能有：遍历一个根目录下的所有目录以及目录下的所有文件；复制所有文件到新的目录结构下，并判断是否重命名。
    :param old_base_folder: 需要移动文件的根目录
    :param is_rename: 移动的文件是否需要重命名，默认是需要重命名
    :param new_folder: 新的文件目录
    :return: 没有返回值
    """
    path_dir = os.listdir(old_base_folder)  # 找根目录下的所有目录或者文件
    print(path_dir)

    i = 1000  # 重命名基数

    if not os.path.exists(new_folder):  # 若新的目录不存在，则创建新的目录
        os.makedirs(new_folder)

    for child_dir in path_dir:  # 遍历根目录下的所有目录或文件
        if os.path.isfile(os.path.join(old_base_folder, child_dir)):  # 针对目录下面的所有文件
            child_file = os.path.join(old_base_folder, child_dir)
            print(child_file)
            if is_rename:
                result_file = new_folder + '/' + str(i) + file_type
                shutil.copyfile(child_file, result_file)  # 复制文件到新的目录下
                i = i + 1
            else:
                result_file = new_folder + '/' + child_dir
                shutil.copyfile(child_file, result_file)

        elif os.path.isdir(os.path.join(old_base_folder, child_dir)):  # 针对目录下面的所有子目录
            child_path = os.path.join(old_base_folder, child_dir)  # 两个目录加起来
            file_all = os.listdir(child_path)  # 找目录下的所有文件
            for file in file_all:  # 遍历目录下的所有文件
                child_file = os.path.join(child_path, file)
                print(child_file)
                if is_rename:
                    result_file = new_folder + '/' + str(i) + file_type
                    shutil.copyfile(child_file, result_file)  # 复制文件到新的目录下
                    i = i + 1
                else:
                    result_file = new_folder + '/' + file
                    shutil.copyfile(child_file, result_file)


if __name__ == '__main__':
    old_base_folder = r"D:\她她她她她她"
    new_folder = r"D:\她她她她她她\sjh"
    move_files_to_new_folder(old_base_folder, new_folder, '.txt')
