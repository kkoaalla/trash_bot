import os
import asyncio
from datetime import datetime
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = os.getenv("TELEGRAM_TOKEN")

user_ids = {
    #"Катя": 123456789,
    "Таня": 1209900390,
    #"Диана Б.": 112233445,
    #"Диана М.": 556677889,
}

# Расписание: ДАТА -> ИМЯ
schedule = {
    "2025-03-27": "Таня",
    "2025-03-29": "Катя",
    "2025-03-30": "Катя",
    "2025-03-31": "Таня",
    "2025-04-01": "Диана Б.",
    "2025-04-02": "Диана Б.",
    "2025-04-03": "Диана М.",
    "2025-04-04": "Диана М.",
    "2025-04-05": "Катя",
    "2025-04-06": "Катя",
    "2025-04-07": "Таня",
    "2025-04-08": "Таня",
    "2025-04-09": "Диана Б.",
    "2025-04-10": "Диана Б.",
    "2025-04-11": "Диана М.",
    "2025-04-12": "Диана М.",
    "2025-04-13": "Катя",
    "2025-04-14": "Катя",
    "2025-04-15": "Таня",
    "2025-04-16": "Таня",
    "2025-04-17": "Диана Б.",
    "2025-04-18": "Диана Б.",
    "2025-04-19": "Диана М.",
    "2025-04-20": "Диана М.",
}

async def send_trash_reminder():
    bot = Bot(token=TOKEN)
    today_str = datetime.now().strftime("%Y-%m-%d")
    person = schedule.get(today_str)

    if person:
        chat_id = user_ids.get(person)
        if chat_id:
            text = f"Привет, {person}! Сегодня твоя очередь вынести мусор 🗑️"
            await bot.send_message(chat_id=chat_id, text=text)
        else:
            print(f"⚠️ Нет chat_id для: {person}")
    else:
        print("Сегодня никому не назначено выносить мусор.")

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_trash_reminder, "cron", hour=23, minute=48)
    scheduler.start()

    print("✅ Бот запущен. Ждём 8:00 каждый день ⏰")
    try:
        while True:
            await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print("🛑 Бот остановлен.")
        print("👋 Выход по Ctrl+C")

if __name__ == "__main__":
    asyncio.run(main())
