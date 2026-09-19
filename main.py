import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib

# 1. Токен, который вы получили от @BotFather
API_TOKEN = '8526804122:AAFQax87qejjYpf0LdoCKzfC_IglRdd0i04'

# 2. Ваш заготовленный список фраз
PHRASES = [
    "Когда апнут саммонеров?",
    "Когда апнут луков?",
    "Когда ножи перестанут убивать магов с одного бэкстаба?",
    "Когда сделают новый чат?",
    "Когда у Саферо отрастут волосы?",
    "Когда Эклипс сотрется об велосипед?"
    "Когда Фрик и Олег перестанут нести бредик?",
    "Когда Лагерта перейдёт в вов классик?",
    "Когда оппонент Умаси наконец то примет вар?",
    "Когда сделают новый чат?",
    "Когда Сирена забалансит?",
    "Когда пофиксят фризы после обновы?"
    "Когда сделают некст таргет?",
    "Когда апнут варлордов?",
    "Когда Кельта перестанет болотить?"
  
  
]

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Хэндлер, который ловит инлайн-запросы
@dp.inline_query()
async def inline_random_phrase(inline_query: types.InlineQuery):
    # Выбираем одну случайную фразу из списка
    random_phrase = random.choice(PHRASES)
    
    # Генерируем уникальный ID для результата (требование Telegram API)
    result_id = hashlib.md5(random_phrase.encode()).hexdigest()
    
    # Формируем элемент инлайн-меню
    item = InlineQueryResultArticle(
        id=result_id,
        title="🤖 Выплюнуть случайную фразу",
        description=f"Нажмите, чтобы отправить: {random_phrase[:30]}...",
        input_message_content=InputTextMessageContent(
            message_text=random_phrase
        )
    )
    
    # Отправляем ответ Telegram (cache_time=0 отключает кэширование, чтобы при каждом открытии фраза менялась)
    await inline_query.answer([item], cache_time=0)

async def main():
    print("Бот запущен и готов плеваться фразами!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
