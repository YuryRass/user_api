# UserAPP

## Инструкция по запуску проекта:

1. Клонировать репозиторий:
```bash
git clone https://github.com/YuryRass/user_api.git
```

2. Перейти в корень проекта:
```bash
cd user_api
```

3. Переименовать файл:
```bash
mv .env-example .env
```

4. Запустить:
```bash
docker compose up --build -d
```

P.S. Миграция базы данных используется в файле [run.sh](script/run.sh) (3-я строка)