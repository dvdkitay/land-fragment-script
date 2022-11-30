import requests
import sys
import uuid
import os
import json
import io
import time

from config.config import MAPS, LANG, SIZE, SKAL, LOGIN, PASSWORD, IP, PORT


def start(PROXIES, FILENAME, MAPS, LANG, SIZE, SKAL):
        
    FILENAME_CREATE_FOLDER = FILENAME.split(".")[0]
    
    # Создаем папку в которую будем сохранять фото
    try:
        os.mkdir(f"pictures/{FILENAME_CREATE_FOLDER}")
    except Exception as error:
        pass
    
    try:
        with open(os.path.join("geojson_data", FILENAME), 'r', encoding='utf-8') as FILE:
            text_to_json = json.loads(FILE.read())

            for j in text_to_json:
            
                    ID = j["id"]
                    X = j["center"]["x"]
                    Y = j["center"]["y"]
                    
                    PROXIES = True if PROXIES == "True" else False
                
                    if PROXIES:
                        PROXIES = {
                            'http': f'http://{LOGIN}:{PASSWORD}@{IP}:{PORT}',
                            'https': f'https://{LOGIN}:{PASSWORD}@{IP}:{PORT}',
                        }
                        api_url = f"https://static-maps.yandex.ru/1.x/?ll={X},{Y}&l={MAPS}&lang={LANG}&z={SKAL}&l=map&size={SIZE}"
                        res = requests.get(api_url, proxies=PROXIES)
                    else:
                        api_url = f"https://static-maps.yandex.ru/1.x/?ll={X},{Y}&l={MAPS}&lang={LANG}&z={SKAL}&l=map&size={SIZE}"
                        res = requests.get(api_url)
                                                        
                    if int(res.status_code) != 200:
        
                        with open(f"logs/geojson_logs.json", "a") as file:
                            current_datetime = time.time()
                            text_log = {
                                "status_code": res.status_code,
                                "id": ID,
                                "x": X,
                                "y": Y,
                                "message": "Карта не может прочитать координаты",
                                "datetime": current_datetime
                            }
                            
                            file.write(str(text_log))

                    else:
                        with io.open(f"pictures/{FILENAME_CREATE_FOLDER}/{ID}.jpg", "wb") as file:
                            file.write(res.content)
                    
                    time.sleep(0.3)
                
    except Exception as err:
        with open(f"logs/system_logs.json", "a") as file:
            current_datetime = time.time()
            text_log = {
                "error": err,
                "mess": "Системная ошибка",
                "datetime": current_datetime
            }
            
            file.write(str(text_log))


if __name__ == '__main__':
    start(
        sys.argv[1],
        sys.argv[2],
        MAPS, LANG, SIZE, SKAL
    )