import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart

from config import Token

bot = Bot(token=Token)
dp = Dispatcher()


buttons = [
    [KeyboardButton(text='BACKEND'), KeyboardButton(text="FRONTEND"),KeyboardButton(text="UX , UI"),KeyboardButton(text="GEEKS")]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.reply(f"Привет {message.from_user.full_name}", reply_markup=keyboard)

@dp.message(Command("help"))
async def help(message: Message):
    await message.reply("Помогу чем смогу /start")


@dp.message(F.text == "BACKEND")
async def greeting(message: Message):
    await message.reply("""Backend — это серверная часть приложения или веб-сайта, отвечающая за обработку данных, бизнес-логику и взаимодействие с базами данных, а также предоставление API для фронтенда (пользовательской части). В backend входят: Backend фактически скрыт от пользователя, но его работа важна для того, чтобы приложение или сайт функционировали корректно.
""")


@dp.message(F.text == "FRONTEND")
async def greeting(message: Message):
    await message.reply("""Frontend — это клиентская (пользовательская) часть веб-приложения или сайта, которая отвечает за отображение данных и взаимодействие с пользователем. Это то, что видит и с чем взаимодействует конечный пользователь через браузер или приложение. Основные элементы фронтенда: Frontend напрямую взаимодействует с пользователем, и его основная задача — сделать приложение простым, быстрым и удобным для пользователя.
""")

@dp.message(F.text == "UX , UI")
async def greeting(message: Message):
    await message.reply("""*UX (User Experience) и UI (User Interface)* — это два ключевых аспекта разработки продукта, направленные на создание удобных и привлекательных интерфейсов для пользователей. Несмотря на тесную связь, они имеют разные задачи и роли в процессе проектирования.
### Различия между UX и UI:
- *UI* — это о том, как выглядит продукт.
- *UX* — это о том, как продукт работает и воспринимается пользователем.

### Основные задачи:
- *UI-дизайнер*: делает продукт визуально привлекательным и следит за эстетикой интерфейса.
- *UX-дизайнер*: делает продукт удобным, логичным и эффективным для выполнения задач пользователя.

Эти дисциплины часто работают в тандеме, так как хороший продукт должен быть не только красивым (UI), но и удобным в использовании (UX).""")

   
@dp.message(F.text == "GEEKS")
async def greeting(message: Message):
    await message.reply("""Международная IT-академия Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым иAndroid-разработчиком Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать возможность каждомучеловеку, даже без опыта в технологиях, гарантированно освоить IT-профессию.

НОМЕР ТЕЛЕФОНА
+996 (557) 05 2018
+996 (507) 05 2018
+996 (777) 05 2018
EMAIL
office@geeks.kg
АДРЕС
ул. Мырзалы Аматова, 1б стр, БЦ "Томирис" (Ор-р:рядом с Драмтеатром) """)




@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понял")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")