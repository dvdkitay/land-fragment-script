import logging
import os
import sys
import io

from lib.sub import Sub
import time

from config.config import MAPS, LANG, SIZE, SKAL, LOGIN, PASSWORD, IP, PORT

logging.basicConfig(
    format='[SCRIPT-DEBUG] %(asctime)s - %(levelname)s: %(message)s',
    level=logging.INFO,
    datefmt='%d-%b-%y %H:%M:%S'
)

def start_stream(PROXIES, MAPS, LANG, SIZE, SKAL):
    
    if PROXIES:
        if not LOGIN or not PASSWORD or not IP or not PORT:
            logging.error("Установите данные для подключения к PROXIES в файле config/config.py")
            return False

    if not MAPS or not LANG or not SIZE or not SKAL:
        logging.error("Установите данные MAPS, LANG, SIZE, SKAL в файле config/config.py")
        return False
        
    try:
        sub = Sub(PROXIES)

        for FILENAME in os.listdir("geojson_data"):
            logging.info(f"Запускаем поток для файла: {FILENAME}")
            stream = sub.starting_a_thread(FILENAME)
            
            if not stream:
                logging.error(f"Ошибка запуска потока для файла: {FILENAME}")
            else:
                logging.info(f"Поток для файла: {FILENAME} запущен. PID процесса: {stream}")
            
            time.sleep(0.3)
            
    except Exception as err:
        logging.error(err)
        
        with open(f"logs/system_logs.json", "a") as file:
            current_datetime = time.time()
            
            text_log = {
                "error": err,
                "datetime": current_datetime
            }
            
            file.write(str(text_log))
            
        return False
    return True


if __name__ == '__main__':
    
    try:
        PROXIES = True if sys.argv[1] == "proxy_enabled" else False
    except:
        PROXIES = False 
    
    if not start_stream(PROXIES, MAPS, LANG, SIZE, SKAL):
        logging.error("Программа завершилась с ошибкой")
    else:
        logging.warning("Программа успешно отработала. Проверте файлы в папке на наличие ошибок /logs")