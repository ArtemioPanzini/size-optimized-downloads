import yadisk
import pandas as pd


# Ваш токен доступа к API Яндекс.Диска
token = "y0_AgAAAABW45BlAAqK2QAAAADtbHj5VaqKl-zjT7GTYDeYnqs91mq5Xas"

# Создайте экземпляр клиента Яндекс.Диска
y = yadisk.YaDisk(token=token)

# Укажите путь к папке на Яндекс.Диске, из которой вы хотите получить файлы
folder_path = "/disk/картинки"

# Параметры запроса
params = {
    "offset": 0,
    "limit" : 100000,
    "type": "file",
    "fields": ["name","public_url"],
}

# Получаем список публичных ресурсов с заданными параметрами
public_resources = y.get_public_resources(**params)

list_dict_article_yandexlink = []
dict_article_yandexlink = {}

# Перебираем каждый ресурс и выводим имена файлов
for resource in public_resources.items:
    name = resource["name"]  # Имя файла
    public_url = resource["public_url"]  # Ссылка на публичный доступ
    dict_article_yandexlink[name] = public_url
    if not name.endswith(".mp4"):  # Исключаем файлы с расширением .mp4
        dict_article_yandexlink[name] = public_url
        
        
result_dict = {}

for key, value in dict_article_yandexlink.items():
    # Извлекаем имя файла без всего после символа "_" и ".jpg"
    name = key.split("_")[0]
    
    # Проверяем, существует ли уже запись с этим именем в словаре
    if name in result_dict:
        result_dict[name].append(value)
    else:
        result_dict[name] = [value]
        
result_dict = {key: value for key, value in result_dict.items() if not key.endswith(".mp4")}

print(result_dict)

# Преобразуем словарь в DataFrame
df = pd.DataFrame(result_dict.items(), columns=['Ключ', 'Значение'])

# Объединим все значения в одной ячейке, разделяя их запятыми
df['Значение'] = df['Значение'].apply(lambda x: ', '.join(x))

# Укажем имя файла для сохранения
output_file = r'C:\Users\LENOVO\size-optimized-downloads\output.xlsx'

# Сохраняем DataFrame в Excel
df.to_excel(output_file, index=False)
print(f'Сохранено в {output_file}')