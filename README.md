# План запуска CLI приложения для аугментации аудио

## Шаг 1: Установка Python
1. Убедитесь, что у вас установлен Python 3.x. Проверить это можно командой:
   ```bash
   python --version
## Шаг 2: Установка необходимых библиотек
```bash
   pip install -r requirements.txt
```
## Шаг 3: Запуск CLI приложения
### Откройте директорию проекта в нем откройте консоль, и ввидите команду
```bash
   python audio_augmentor.py /path/to/input/file.mp3 /path/to/output/file.wav
```
### Здесь:
/path/to/input/file.mp3 — это путь к исходному аудио файлу .mp3.

/path/to/output/file.wav — это путь, куда будет сохранен аугментированный аудио файл. Убедитесь, что указали путь с расширением .wav.
обратите внимание на то что фаил должен быть на латинице, на Русском не работает, без пробелов.
## Шаг 2: Пример использования CLI
```bash
python main.py C:\Users\svetl\Desktop\akim-apachev-leto-i-arbalety.mp3 new-akim-apachev-leto-i-arbalety.wav


   
