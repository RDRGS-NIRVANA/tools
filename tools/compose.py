import os
from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment

# 定义视频文件夹和音频文件夹路径
video_folder = "/path/to/video_folder/"
audio_folder = "/path/to/audio_folder/"


def compose_audio_to_video(video_folder, audio_folder):
    # 遍历视频文件夹中的所有文件
    for video_file in os.listdir(video_folder):
        video_path = os.path.join(video_folder, video_file)

        # 检查文件是否为视频文件
        if video_file.endswith((".mp4", ".avi", ".mkv")):
            # 遍历音频文件夹中的所有文件
            for audio_file in os.listdir(audio_folder):
                audio_path = os.path.join(audio_folder, audio_file)

                # 检查文件是否为音频文件
                if audio_file.endswith((".mp3", ".wav")):
                    # 加载视频和音频文件
                    video = VideoFileClip(video_path)
                    audio = AudioFileClip(audio_path)

                    # 从视频中提取视频轨道（去除音频）
                    video_without_audio = video.without_audio()

                    # 将音频替换为新音频
                    video_with_new_audio = video_without_audio.set_audio(audio)

                    # 输出替换后的视频文件
                    output_video_path = os.path.join(video_folder, "new_" + video_file)
                    video_with_new_audio.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

                    # 一对一替换完成后退出内层循环继续下一个视频文件
                    break


def audio_to_long(audio_folder, output_folder):
    # 遍历音频文件夹中的所有文件
    audio_files = os.listdir(audio_folder)
    num_files = len(audio_files)

    # 设置每组合成的音频文件数量
    group_size = 6

    # 计算总共需要合成的组数
    num_groups = num_files // group_size

    for group_index in range(num_groups):
        # 创建一个空的音频段，作为合成组的音频容器
        combined_audio = AudioSegment.silent(duration=0)

        # 计算当前组的起始索引和结束索引
        start_index = group_index * group_size
        end_index = (group_index + 1) * group_size

        # 遍历当前组的音频文件
        for audio_file in audio_files[start_index:end_index]:
            audio_path = os.path.join(audio_folder, audio_file)

            # 检查文件是否为音频文件
            if audio_file.endswith((".mp3", ".wav")):
                # 加载音频文件
                audio = AudioSegment.from_file(audio_path)

                # 将当前音频文件添加到合成组的音频容器中
                combined_audio += audio

        # 构造当前组的输出文件名
        output_file = f"group_{group_index}.wav"
        output_path = os.path.join(output_folder, output_file)

        # 导出合成后的音频文件
        combined_audio.export(output_path, format="wav")


def audio_duration(audio_file):
    # 加载音频文件
    audio = AudioSegment.from_file(audio_file)

    # 获取音频长度（单位：毫秒）
    duration = len(audio)

    return duration


if __name__ == '__main__':
    audio_to_long(r'C:\Users\dev1se\Downloads\cry', r'C:\Users\dev1se\Downloads\new')
    # audio_file = r"C:\Users\dev1se\Downloads\new\group_0.wav"
    # print(f"音频长度为 {audio_duration(audio_file)} 毫秒")
