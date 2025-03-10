  # Space image downloader

Этот проект позволяет скачивать фотографии космоса Nasa и SpaceX и публиковать их в Telegram канале с заданной переодичностью.


## Установка зависимостей
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Установка переменных окружения 
Создайте файл secrets.env в корневой директории проекта и добавьте в него следущие переменные:

1. API_NASA=<API_TOKEN> [https://api.nasa.gov/]

2. API_EARTH=<API_TOKEN> [https://api.nasa.gov/#epic]

3. API_TELEBOT=<API_TOKEN> [https://telegram.me/BotFather]

4. PUBLISH_DELAY_HOURS=<раз в сколько часов отправлять фото>

5. CHAT_ID = <ID_CHAT> - получите id чата telegram

## Cкрипты:
1. ### fetch_earth_image.py
Скрипт скачивает фотографии земли с космоса. Нужно указать количество фото. 
```
    fetch_earth_image <Количество>
```
2. ### fetch_nasa_photo.py
Скрипт скачивает фотографии Nasa. Нужно указать количество фото.
```
fetch_nasa_photo.py <Количество>
```

3. ### fetch_spacex_images.py
Этот скрипт скачивает фотографии с последних запусков SpaceX. Указать айди запуска, по умолчанию последний
```
fetch_spacex_images.py <id>
```

4. ### utils.py

Вспомогательный скрипт

5. ### telebot.py
Запускает бота
## Пример работы проекта ##

1. Скачиваем 5 фото

```
python fetch_nasa_photo.py 5
```

2. Публикуем изображение в Telegram (каждые 4 часа по умолчанию)
```
python telebot.py
```

