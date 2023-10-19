import requests
import os
import shutil
from logs_LightStar import logging_config_lightstar
from datetime import datetime 

common_logger = logging_config_lightstar.common_logger

def move_file_if_exists(source_path, target_directory):
    if os.path.isfile(source_path):
        # Имя файла из пути
        file_name = os.path.basename(source_path)
        timestamp = datetime.now().strftime("%m_%d-%H-%M-%S")
        new_file_name = f"{timestamp}_{file_name}"

        
        # Полный путь к новому местоположению файла в целевой директории
        new_file_path = os.path.join(target_directory, new_file_name)

        # Перемещаем файл в целевую директорию
        shutil.move(source_path, new_file_path)

        common_logger.info(f'Файл перемещен в {new_file_path}')

def download_file(file_url, target_path):
    response = requests.get(file_url)

    if response.status_code == 200:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        with open(target_path, 'wb') as file:
            file.write(response.content)
            
        common_logger.info(f'Файл скачан и сохранен в {target_path}')
    else:
        common_logger.error(f'Не удалось скачать файл. Код статуса: {response.status_code}')

def main():
    # URL файла для загрузки
    file_url = 'https://lightstar.ru/image/yml/lightstar_rozn_dolgop_stock.yml'

    # Полный путь к текущему скрипту
    script_directory = os.path.dirname(__file__)

    # Папка для сохранения загруженных файлов
    download_folder = os.path.join(script_directory, '../data/LightStar/')
    
    # Имя файла из URL
    file_name = os.path.basename(file_url)

    # Полный путь к файлу для сохранения
    file_path = os.path.join(download_folder, file_name)

    # Полный путь к целевой директории (data_done)
    target_directory = os.path.join(script_directory, '../data/LightStar/data_done/')

    move_file_if_exists(file_path, target_directory)
    download_file(file_url, file_path)

if __name__ == '__main__':
    main()