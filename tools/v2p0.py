import cv2
import os


def extract_frames_from_video(video_path, output_folder):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 获取视频帧数
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_count = 0
    while True:
        ret, frame = cap.read()
        # if not ret:
        if frame_count == 1:
            break
        file_name = os.path.basename(video_path)
        # 保存图片
        output_path = os.path.join(output_folder, f"{file_name}_{frame_count}.jpg")
        cv2.imwrite(output_path, frame)

        frame_count += 1
        print(f"已处理帧数：{frame_count}/{total_frames}")

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


def extract_first_frame(video_path, output_path):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 读取第一帧
    ret, frame = cap.read()

    # 保存第一帧为图像文件
    cv2.imwrite(output_path, frame)

    # 释放资源
    cap.release()


def crop_and_save_rectangle(input_path, output_path, x1, y1, x2, y2):
    # 打开视频文件
    video_name = os.path.splitext(os.path.basename(input_path))[0]
    output_picture_path = output_path + "\\" + video_name + "\\"
    if not os.path.exists(output_picture_path):
        os.makedirs(output_picture_path)

        video_capture = cv2.VideoCapture(input_path)

        # 设置保存图片的计数器
        image_count = 1

        # 定位到起始帧
        start_frame = 0
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        # 循环读取视频帧并保存裁剪的矩形区域
        frame_count = start_frame
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            # 裁剪矩形区域
            cropped_frame = frame[int(y1):int(y2), int(x1):int(x2)]

            # 保存裁剪的图片
            output_file = output_picture_path + "/" + str(image_count) + ".jpg"
            cv2.imwrite(output_file, cropped_frame)

            image_count += 1
            frame_count += 1

        # 释放视频捕捉对象
        video_capture.release()


if __name__ == '__main__':
    # 指定多个视频的路径和输出文件夹
    output_folder = r"C:\Users\dev1se\Desktop\pic"
    # 指定文件夹路径
    folder_path = r"C:\Users\dev1se\Desktop\yolov5-master\data\videos\cry"

    # 获取文件夹下所有文件路径
    file_paths = get_all_file_paths(folder_path)

    for video_path in file_paths:
        # 拆解视频为图片
        extract_frames_from_video(video_path, output_folder)
