# Short-URL

Short URL Service — это микросервис на базе FastAPI для создания коротких ссылок, редиректа по коротким ссылкам и предоставления статистики по ним. Данные хранятся в SQLite.

---

## Функциональность

1. **POST /shorten**: Принимает длинный URL (JSON: `{"url": "<ваш URL>"}`) и возвращает короткий идентификатор.
2. **GET /{short_id}**: Перенаправляет на полный URL по короткому идентификатору.
3. **GET /stats/{short_id}**: Возвращает JSON с информацией о полном URL.

Примеры работы API можно найти в Swagger-документации по адресу `/docs`.

---

## Запуск проекта

### Локальный запуск

#### 1. Установите зависимости
Создайте виртуальное окружение (опционально) и установите зависимости из `requirements.txt`:

pip install -r requirements.txt

Запуск:

uvicorn main:app --reload

Откройте приложение:

http://127.0.0.1:8000/docs


### Через Docker

скачайте Docker из Docker Hub

Выполните команду:

docker volume create shorturl_data

Запустите контейнер:

docker run -d -p 8000:80 -v shorturl_data:/app/data <ваш_логин>/shorturl-service:latest


****
