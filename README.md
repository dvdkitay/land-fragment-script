<div align="left">
<img src="https://img.shields.io/github/languages/code-size/dvdkitay/land-fragment-script" />
<img src="https://img.shields.io/github/languages/top/dvdkitay/land-fragment-script" />
<img src="https://img.shields.io/github/issues/dvdkitay/land-fragment-script" />
<img src="https://img.shields.io/github/issues-pr/dvdkitay/land-fragment-script" />
<div>

![Иллюстрация к проекту](https://raw.githubusercontent.com/dvdkitay/land-fragment-script/master/pictures/file1/1.jpg)

## Скрипт для обрезания карты по координатам

Программа для получения снимков с карты земли по координатам в необходимом размере

## Как работает скрипт 

<li>Скрипт получает все файлы из папки `geojson_data` и запускает отдельный поток для каждого файла отдельно 

<li>Логирование ошибок при `status_code != 200`, а также системные ошибки

<li>Ошибки связанные с координами записываются в файл логов `/log/geojson_logs.json`

<li>Ошибки связанные с системой записываются в файл логов `/log/system_logs.json`

Для удобства файл с ошибками `/log/geojson_logs.json`, записывается в удобном формате для возможности проверить координаты вручную

## Результат успешного запуска

```
[SCRIPT-DEBUG] 27-Nov-22 19:48:33 - INFO: Запускаем поток для файла: file1.json
[SCRIPT-DEBUG] 27-Nov-22 19:48:33 - INFO: Поток для файла: file1.json запущен. PID процесса: 35083
[SCRIPT-DEBUG] 27-Nov-22 19:48:33 - WARNING: Программа успешно отработала
```

## Описание файлов и каталогов

```
/config - В данной папке config.py - конфигурация программы
/geojson_data - В данную папку необходимо поместить файлы *.json
/lib - В данной папке находится класс запуска потоков
/pictures - В эту папку будут сохраняться сохраненные фото по координатам
/stream - В этой папке находится файл который запускается в поток
/log - Файл логов
stream.py - Файл который запускается в поток 
app.py - Главный файл запуска приложения
```

## Возможные ошибки
Если не установлена одна из конфигураций в `config/config.py`

```
[SCRIPT-DEBUG] 27-Nov-22 19:44:22 - ERROR: Установите данные MAPS, LANG, SIZE, SKAL в файле config/config.py
[SCRIPT-DEBUG] 27-Nov-22 19:44:22 - ERROR: Программа завершилась с ошибкой
```

Если скрипт запущен с прокси, но не установлена конфигурация подключения к прокси в `config/config.py`

```
[SCRIPT-DEBUG] 27-Nov-22 19:46:26 - ERROR: Установите данные для подключения к PROXIES в файле config/config.py
[SCRIPT-DEBUG] 27-Nov-22 19:46:26 - ERROR: Программа завершилась с ошибкой
```

## Подготовка

1. Подготовте файлы в формат `.json`. Пример файла лежит в папке `geojson_data/file1.json`
2. Перенестите в папку `geojson_data`

При сохранении картинок скрипт будет создавать в папке `pictures` папки с именем файла и туда сохранять картинки с именами файлов равными `id` из файла по каждым координатам

## Конфигурация

Установить конфигурацию в файле `config/config.py`

```
# Слои и типы карты
MAPS = "sat" 

# Локализация карты
LANG = "en_US"

# Размер выходной картинки (Максимальный 650х450)
SIZE = "450,450"

# Масштаб
SKAL = "12"

# Конфигурация прокси
LOGIN = ""
PASSWORD = ""
IP = ""
PORT = ""
```

## Запуск

Ограничения по запросам 25000 в сутки. При необходимости увелечения запросов запускайте с прокси. 

Для запуска с прокси передайте системный аргумент `proxy_enabled`

```
python3 app.py proxy_enabled
```

Для запуска без прокси 

```
python3 app.py 
```