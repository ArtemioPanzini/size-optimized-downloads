import moviepy.editor as mp
import os

# Папка с видеофайлами для обработки
input_folder = r'C:\Users\LENOVO\size-optimized-downloads\videos\video_31mb'

# Папка для сохранения обработанных видеофайлов
output_folder = r'C:\Users\LENOVO\size-optimized-downloads\videos\videos_less31mb'

# Проверяем, существует ли папка для сохранения, и создаем ее, если она не существует
os.makedirs(output_folder, exist_ok=True)

# Проходимся по всем файлам в папке
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):  # Проверяем, что файл - видео с расширением .mp4
        input_path = os.path.join(input_folder, filename)
        
        # Получаем имя файла без расширения
        video_name = os.path.splitext(filename)[0]

        # Создаем объект VideoFileClip
        clip = mp.VideoFileClip(input_path)

        # Формируем путь для сохранения обработанного видео
        output_path = os.path.join(output_folder, video_name + '.mp4')

        # Выполняем операции с видео (например, сохранение)
        clip.write_videofile(output_path)

        # Освобождаем ресурсы
        clip.close()

print("Обработка завершена")
