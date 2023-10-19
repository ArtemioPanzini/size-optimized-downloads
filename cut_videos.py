from moviepy.editor import VideoFileClip
import os

# Папка с видеофайлами для обработки
input_folder = r'C:\Users\LENOVO\size-optimized-downloads\videos\videos_less31mb'

# Папка для сохранения обработанных видеофайлов
output_folder = r'C:\Users\LENOVO\size-optimized-downloads\videos\videos_cutted_low_quality'

# Проходимся по всем файлам в папке
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):  # Проверяем, что файл - видео с расширением .mp4
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename )
        
        # Открываем видеофайл с использованием moviepy
        video = VideoFileClip(input_path)
        
        # Изменяем размер видео
        resized_video = video.resize((1920, 1080))
        
        # Сохраняем видео с аудио в формате MP4
        resized_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

print("Обработка завершена.")
