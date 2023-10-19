import pandas as pd
import requests
import os

# Загрузите данные из Excel-файла
excel_file = r'C:\Users\LENOVO\size-optimized-downloads\download_img\Ссылки на картинки.xlsx'
df = pd.read_excel(excel_file)

# Создайте директорию для сохранения изображений, если её нет
output_directory = r'C:\Users\LENOVO\size-optimized-downloads\download_img\картинки'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Пройдитесь по строкам таблицы
for index, row in df.iterrows():
    # Получите значение из столбца "артикул"
    артикул = row['Артикул']
    
    # Переберите столбцы с ссылками на изображения (столбцы 1-20 включительно)
    for i in range(1, 20):
        # Получите ссылку на изображение
        ссылка = row[i]
        
        # Если ссылка есть
        if not pd.isna(ссылка):
            # Создайте имя файла, заменив "/" на "-"
            имя_файла = f'{артикул.replace("/", "-")}_{i}.jpg'
            
            # Полный путь к файлу
            полный_путь = os.path.join(output_directory, имя_файла)
            
            # Скачайте изображение и сохраните его
            response = requests.get(ссылка)
            if response.status_code == 200:
                with open(полный_путь, 'wb') as f:
                    f.write(response.content)
                print(f'Изображение для артикула {артикул} ({i-1}) сохранено как {имя_файла}')
            else:
                print(f'Ошибка при загрузке изображения для артикула {артикул} ({i-1})')

print('Завершено')
