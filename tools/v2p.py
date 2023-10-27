import cv2
import os


def extract_16frames_from_75video(video_path, output_folder):  # 从75帧提取16帧
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 获取视频帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames >= 72:
        # 创建输出文件夹
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        video_name = os.path.splitext(os.path.basename(video_path))[0]
        output_picture_path = output_folder + "\\" + video_name + "\\"

        if not os.path.exists(output_picture_path):
            os.makedirs(output_picture_path)

        frame_count = 0
        save_count = 0
        next_save = 0
        while save_count < 16:
            ret, frame = cap.read()
            if frame_count == next_save:
                # if not ret:
                if save_count % 2 == 0:
                    next_save = next_save + 4
                else:
                    next_save = next_save + 5

                # 保存图片
                output_path = os.path.join(output_picture_path, f"{save_count}.jpg")
                cv2.imwrite(output_path, frame)
                save_count += 1
            frame_count += 1

        # 释放资源
        cap.release()

        print("拆解完成！")


def get_all_file_paths(folder_path):
    file_paths = []

    # 遍历文件夹下的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        # 遍历当前文件夹下的所有文件
        for file_name in files:
            # 构建文件的完整路径
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)

    return file_paths

if __name__ == '__main__':
    # 指定多个视频的路径和输出文件夹
    output_folder = r"E:\Infant\picture"
    # 指定文件夹路径
    folder_path = r"E:\Infant\Right_leg+Right_hand"

    # 获取文件夹下所有文件路径
    file_paths = get_all_file_paths(folder_path)

    for video_path in file_paths:
        # 拆解视频为图片
        extract_16frames_from_75video(video_path, output_folder)
