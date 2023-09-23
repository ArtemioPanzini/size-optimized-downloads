import os
import requests
import moviepy.editor as mp
import time
import logging

# Получаем путь к папке, где находится этот скрипт
script_folder = os.path.dirname(os.path.abspath(__file__))

# Настройки логгирования
log_filename = os.path.join(script_folder, "scrapping.log")
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

def create_dict_from_txt(txt_file_path):
    result_dict = {}
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as txtfile:
            for line in txtfile:
                line = line.strip()
                if line:
                    key, value = line.split(': ', 1)
                    result_dict[key] = value
        return result_dict
    except FileNotFoundError:
        logging.error(f'Файл "{txt_file_path}" не найден.')
        return None
    except Exception as e:
        logging.error(f'Произошла ошибка при чтении файла: {str(e)}')
        return None


def download_video(video_dict):
    output_folder = os.path.join(script_folder, "videos")
    output_folder2 = os.path.join(script_folder, "videos", "video_fin")
    
    # Проверяем существование папок и создаем их, если они не существуют
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(output_folder2):
        os.makedirs(output_folder2)
        
    for video_name, video_url in video_dict.items():
        if not os.path.exists(os.path.join(output_folder2, video_name + '.mp4')):  # Проверяем, что видео не было уже скачано
            for attempt in range(2):  # Две попытки с интервалом в 60 секунд
                    response = requests.get(video_url)
                    if response.status_code == 200:
                        video_path = os.path.join(output_folder, video_name + '.mp4')  # Добавляем расширение .mp4
                        with open(video_path, 'wb') as video_file:
                            video_file.write(response.content)
                        logging.info(f'Видео "{video_name}" успешно скачано.')
                        
                        # Вызываем функцию для конвертации видео и удаления исходного файла
                        convert_and_delete_video(video_path, video_name)
                        break  # Выходим из цикла после успешной загрузки
                    else:
                        if attempt == 0:
                            logging.error(f'Не удалось скачать видео "{video_name}". Попытка {attempt + 1}. Статус код: {response.status_code}')
                        else:
                            logging.error(f'Не удалось скачать видео "{video_name}". Попытка {attempt + 1}. Повторная попытка через 60 секунд...')
                            time.sleep(60)  # Ждем 60 секунд перед повторной попыткой

def convert_and_delete_video(input_path, video_name):
    try:
        clip = mp.VideoFileClip(input_path)
        output_folder = os.path.join(script_folder, "videos", "video_fin")
        output_path = os.path.join(output_folder, video_name + '.mp4')
        clip.write_videofile(output_path)
        logging.info(f'Видео "{video_name}" успешно сконвертировано и сохранено в папке "{output_folder}".')
        
        # Удаляем исходный видеофайл
        os.remove(input_path)
        logging.info(f'Исходный файл "{video_name}" удален.')
        with open(success_file_path, 'a', encoding='utf-8') as success_file:
            success_file.write(f'{video_name}\n')
    except Exception as e:
        logging.error(f'Произошла ошибка при конвертации видео "{video_name}": {str(e)}')


success_file_path = os.path.join(script_folder, "successful_articles.txt")
txt_file_path = os.path.join(script_folder, 'результат_dict.txt')
result_dict = create_dict_from_txt(txt_file_path)

download_video(result_dict)