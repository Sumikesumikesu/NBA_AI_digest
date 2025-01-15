#!/bin/bash

echo "Создание виртуального окружения..."
python -m venv venv

echo "Активация виртуального окружения..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
  # Windows (Git Bash)
  source venv/Scripts/activate
else
  # macOS/Linux
  source venv/bin/activate
fi


echo "Установка зависимостей..."
if [[ -f "requirements.txt" ]]; then
  pip install -r requirements.txt
else
  echo "Файл requirements.txt не найден. Убедитесь, что зависимости установлены вручную."
fi

echo "Деактивация виртуального окружения..."
deactivate

echo "Скрипт завершен."