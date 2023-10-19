import os


debug_list = []

def check_video_folder(directory_path):
    try:
        # Получаем список файлов в указанной директории
        files = os.listdir(directory_path)

        # Перебираем файлы и проверяем их размер
        for file_name in files:
            file_path = os.path.join(directory_path, file_name)
            file_size = os.path.getsize(file_path)  # Размер файла в байтах

            # Проверяем, если размер файла больше 30 МБ (30 * 1024 * 1024 байт)
            if file_size > 30 * 1024 * 1024:
                debug_list.append(file_name)
                # Если хотя бы один файл больше 30 МБ, возвращаем False
        
        if debug_list:
            print(debug_list)
            return False
        else:
            return True  # Если все файлы меньше 30 МБ, возвращаем True
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return False

# Относительный путь к директории video_fin относительно местоположения скрипта
video_fin_directory = os.path.join(os.path.dirname(__file__), "videos/video_fin")

# Проверяем папку и выводим результат
result = check_video_folder(video_fin_directory)
if result:
    print("Папка готова: True")
else:
    print("Папка готова: False")