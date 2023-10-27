import cv2
import os
import ffmpeg

def images_to_video(input_folder, output_path):
    # 读取文件夹中的所有图片文件
    folder_name = os.path.basename(input_folder)

    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    # image_files.sort()  # 按文件名排序，保证顺序正确
    sorted_names = sorted(image_files, key=lambda x: int(x.split('.')[0]))
    # 读取第一张图片，获取图像尺寸
    first_image = cv2.imread(os.path.join(input_folder, sorted_names[0]))
    height, width, _ = first_image.shape

    # 创建视频编码器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path+"\\"+folder_name+".mp4", fourcc, 25, (width, height))

    # 遍历所有图片并写入视频
    for image_file in sorted_names:
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)
        video_writer.write(image)

    # 释放资源
    video_writer.release()

    print(f"{folder_name}合成完成")

def traverse_folder(folder_path):
    folder_list = []
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            folder_list.append(os.path.join(root, dir))
    return folder_list

# 指定输入文件夹和输出视频路径
input_folder = r'C:\Users\dev1se\Desktop\yolov5-master\runs\infant_pictures_notcry'
output_path = r'C:\Users\dev1se\Desktop\yolov5-master\runs\infant_videos_notcry'

folder_list = traverse_folder(input_folder)
# 调用函数进行图片合成视频
for folder in folder_list:
    images_to_video(folder, output_path)
