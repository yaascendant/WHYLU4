import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# 1. ТОКЕН БОТА
API_TOKEN = '8526804122:AAFQax87qejjYpf0LdoCKzfC_IglRdd0i04'

# 2. СПИСОК ФРАЗ
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

@dp.inline_query()
async def inline_random_phrase(inline_query: types.InlineQuery):
    random_phrase = random.choice(PHRASES)
    result_id = hashlib.md5(random_phrase.encode()).hexdigest()
    
    item = InlineQueryResultArticle(
        id=result_id,
        title="Когда на луче....?",
        description=f"Когда же?",
        input_message_content=InputTextMessageContent(message_text=random_phrase)
    )
    await inline_query.answer([item], cache_time=0)

# --- ЖИЗНЕННО НЕОБХОДИМЫЙ КОСТЫЛЬ ДЛЯ БЕСПЛАТНОГО RENDER ---
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_fake_server():
    # Render по умолчанию выдает порт 10000 для Web Service
    server = HTTPServer(('0.0.0.0', 10000), SimpleHTTPRequestHandler)
    server.serve_forever()
# -----------------------------------------------------------

async def main():
    # Запускаем фальшивый сервер в фоновом потоке
    threading.Thread(target=run_fake_server, daemon=True).start()
    
    print("Бот запущен и готов плеваться фразами!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
