import yadisk

# Ваш токен доступа к API Яндекс.Диска
token = "y0_AgAAAABW45BlAAqK2QAAAADtbHj5VaqKl-zjT7GTYDeYnqs91mq5Xas"

# Создайте экземпляр клиента Яндекс.Диска
y = yadisk.YaDisk(token=token)

# Укажите путь к папке на Яндекс.Диске, в которой находятся файлы, которые вы хотите сделать публично доступными
folder_path = "/картинки"

# Получите информацию о содержимом папки
folder_info = y.listdir(folder_path)

# Переберите каждый элемент в папке
for item in folder_info:
    if item.type == "file":
        # Получите путь к файлу
        file_path = item.path
        
        # Сделайте файл публично доступным
        y.publish(file_path)
        
        # Получите публичную ссылку на файл
        public_url = y.get_download_link(file_path)
        
        # Выведите публичную ссылку
        print(f"Публичная ссылка на файл '{item.name}': {public_url}")