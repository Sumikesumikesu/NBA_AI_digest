#!/bin/bash

# echo "Переход в директорию проекта..."
# cd /path/to/your/project_folder

echo "Активация виртуального окружения..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
  # Windows (Git Bash)
  source venv/Scripts/activate
else
  # macOS/Linux
  source venv/bin/activate
fi

# 3. Запуск main.py
echo "Запуск main.py..."

echo "\n----------"
python main.py
echo "\n----------"

# 4. Деактивация виртуального окружения
echo "Деактивация виртуального окружения..."
deactivate

echo "Скрипт завершен."