from moviepy.video.io.VideoFileClip import VideoFileClip
import os


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


def video_to_audio(video_path, audio_folder):
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    # 读入视频文件
    video = VideoFileClip(video_path)
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    # 提取视频中的音频
    audio = video.audio

    audio_path = audio_folder + "\\other_" + video_name + ".mp3"
    # 将音频输出为 MP3 文件
    audio.write_audiofile(audio_path)


if __name__ == '__main__':
    # 指定多个视频的路径和输出文件夹
    output_folder = r"C:\Users\dev1se\Desktop\AudioClassification-Pytorch-master\infant_audio\other_cry"
    # 指定文件夹路径
    folder_path = r"C:\Users\dev1se\Desktop\InfantMulti\data\infant\other_cry"

    # 获取文件夹下所有文件路径
    file_paths = get_all_file_paths(folder_path)

    for video_path in file_paths:
        # 拆解视频为图片
        video_to_audio(video_path, output_folder)
