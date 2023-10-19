data_list = [
    {"Имя": "1005-05-05p_1.jpg", "Тип": "https://yadi.sk/i/A_HAnPVfYHKLkw"},
    {"Имя": "1005-05-05p_2.jpg", "Тип": "https://yadi.sk/i/hid7-FjyRzJW_Q"},
    {"Имя": "1005-05-05p_3.jpg", "Тип": "https://yadi.sk/i/hid141yRzJW_Q"}
]

result_dict = {}

# Проходимся по словарям в списке
for item in data_list:
    name = item["Имя"]
    link = item["Тип"]
    
    # Извлекаем имя файла без всего после символа "_"
    name = name.split("_")[0] + ".jpg"
    
    # Проверяем, существует ли уже запись с этим именем в словаре
    if name in result_dict:
        result_dict[name].append(link)
    else:
        result_dict[name] = [link]

print(result_dict)