import yadisk

# Ваш токен доступа к API Яндекс.Диска
token = "y0_AgAAAABW45BlAAqK2QAAAADtbHj5VaqKl-zjT7GTYDeYnqs91mq5Xas"

# Создайте экземпляр клиента Яндекс.Диска
y = yadisk.YaDisk(token=token)

# Укажите путь к папке на Яндекс.Диске, которую вы хотите исследовать
folder_path = "/Картинки Стилфорт"

# Получите информацию о содержимом папки
folder_info = y.listdir(folder_path)

# Переберите каждый элемент в папке
for item in folder_info:
    item_name = item["name"]  # Имя элемента
    item_type = item["public_url"]  # Тип элемента (file или dir)

    # Делайте что-то с элементом, например, выведите его имя и тип
    print(f"Имя: {item_name}, Тип: {item_type}")