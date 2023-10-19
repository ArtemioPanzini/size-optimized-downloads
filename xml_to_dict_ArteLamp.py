
import xml.etree.ElementTree as ET
import os
from datetime import datetime 




def main():
    script_directory = os.path.dirname(__file__)
    download_folder = os.path.join(script_directory, '../data/ArteLamp/')
    file_path = os.path.join(download_folder, 'lobachev_technolightru_yandex.xml')
    xml_file_path = file_path
    
    prices_data_ArteLamp = []
    stocks_data_ArteLamp = []
    try:
        # Разбор XML-файла
        tree = ET.parse(xml_file_path)

        root = tree.getroot()
                  
        # Создание списка для хранения отдельных <offer> элементов
        offers = {}
        date_now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+02:00')
          

        # Поиск всех элементов <offer>
        for offer_element in root.findall('.//offer'):
            
            article = offer_element.find('.//vendorCode').text
            article = article.replace(" ","-")
            price_full_str = offer_element.find('.//price').text
            price_full = float(price_full_str)
            price = round(price_full * 0.9)
            
                
            overleft = 0
            outlet_element = offer_element.find('.//stock').text
            
            if outlet_element is not None:

                try: 
                    outlet_element = offer_element.find('.//stock').text
                    overleft = round(float(outlet_element))
                    if overleft == 1:
                        overleft = 0
                except Exception as e:
                    pass
                    #common_logger.info(f'Ошибка {e} во время разбора {article}')

            price_data = {
                "offerId": f"{article}",
                "price": {
                    "value": float(price),
                    "currencyId": "RUR"
                }
            }              
                        
            stocks_data = {
                        "sku": f"{article}",
                        "warehouseId": 764952,
                        "items": [
                            {
                            "count": overleft,
                            "type": "FIT",
                            "updatedAt": date_now,
                            }
                        ]
                        }
            
            prices_data_ArteLamp.append(price_data)
            stocks_data_ArteLamp.append(stocks_data)
        return prices_data_ArteLamp, stocks_data_ArteLamp
        
    except Exception as e:
        pass
