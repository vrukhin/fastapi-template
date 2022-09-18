# Запуск через shell

1. Установите Poetry `pip install poetry`
1. Активируйте виртуальное окружение `poetry shell`
1. Установите зависимости `poetry install`
1. Запустите приложение `uvicorn app.main:app --reload`

# Запуск через контейнер

1. Установите Docker
1. Добавьте пользователя в группу **docker**
1. Соберите контейнер `docker build -t myimage .`
1. Запустите контейнер `docker run -d --name mycontainer -p 80:80 myimage`
1. Последующий запуск контейнера выполняется командой `docker start`
