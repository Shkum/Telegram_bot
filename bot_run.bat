@echo off

call %~dp0venv\Scripts\activate

cd %~dp0

set TOKEN=5433931992:AAG7ykhximKcgFz-SY6-zjNenTVQ7X4h0dQ

python Telegram_bot.py

pause
