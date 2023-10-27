from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os
import cv2


def split_video(file_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 打开视频文件
    video = VideoFileClip(file_path)
    video_name = os.path.splitext(os.path.basename(file_path))[0]
    # 计算每个片段的时长
    segment_duration = 3

    # 获取视频的总时长
    total_duration = video.duration

    # 初始化片段起始和结束时间
    start_time = 1080
    end_time = start_time + segment_duration

    # 初始化片段索引
    segment_count = 0

    while end_time <= total_duration:
        # 切割视频
        segment = video.subclip(start_time, end_time)

        # 保存视频片段
        if segment_count < 10:
            segment_filename = f'{output_path}\\{video_name}_00{segment_count}.mp4'
        elif segment_count < 100:
            segment_filename = f'{output_path}\\{video_name}_0{segment_count}.mp4'
        elif segment_count < 1000:
            segment_filename = f'{output_path}\\{video_name}_{segment_count}.mp4'

        segment.write_videofile(segment_filename)

        # 更新起始和结束时间
        start_time += segment_duration
        end_time += segment_duration

        # 增加片段索引
        segment_count += 1

    # 关闭视频文件
    video.close()


def split_video2(file_path, output_path):
    start_time = 0
    end_time = segment_duration
    clip_num = 0
    video_name = os.path.splitext(os.path.basename(file_path))[0]
    while start_time < video_duration:
        if clip_num < 10:
            output_file = f"{output_path}\\{video_name}_00{clip_num}.mp4"
        elif clip_num < 100:
            output_file = f"{output_path}\\{video_name}_0{clip_num}.mp4"
        elif clip_num < 1000:
            output_file = f"{output_path}\\{video_name}_{clip_num}.mp4"
        ffmpeg_extract_subclip(file_path, start_time, end_time, targetname=output_file)
        print(f"Saved {output_file}")

        start_time = end_time
        end_time += segment_duration
        clip_num += 1


# 设置视频文件路径和每个片段的时长（单位：秒）
video_file = r"E:\大学\dataset\2023-10-19-Video\20230727\00000001690000000.mp4"
video_name = os.path.splitext(os.path.basename(video_file))[0]
output_folder = fr"E:\大学\dataset\infant_cry\{video_name}"
segment_duration = 3.0
#
# # 获取视频总时长
video_duration = VideoFileClip(video_file).duration

# 切分视频
split_video(video_file, output_folder)
