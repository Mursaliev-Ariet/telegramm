from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import os

TOKEN = os.getenv("TOKEN")
# =======================
# 📚 ДАННЫЕ ПОРОД
# =======================
cats = {
    "mainecoon": {
        "name": "🐱 Мейн-кун",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToqCNZWn6UQSA7S8BIYOblnYinHG6PTksCbNe5qe7qBw&s",
        "text": "Крупная, пушистая кошка с мощным телом и кисточками на ушах.Характер: умный, спокойный, дружелюбный. Хорошо ладит с детьми и другими животными."
    },
    "persid": {
        "name": "🐱 Персидская кошка",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfyBwAmeGz9zLpjj--WRvKIxkkJYR8EY2BEuS1zQVmkQ&s=10",
        "text": "Очень пушистая с плоской мордой.Характер: спокойная, домашняя, любит тишину и комфорт. Требует ухода за шерстью."
    },
    "norweg": {
        "name": "🐱 Норвежская лесная кошка",
        "photo": "https://yac-wh-sb-prod-s3-media-07001.storage.yandexcloud.net/media/images/norvezhskaya-lesnaya3.max-2880x1820.format-jpeg_a96OihF.jpg",
        "text": "Крепкая, выносливая, с густой шерстью.Характер: независимая, умная, хорошо адаптируется к холодному климату."
    },
    "turkey": {
        "name": "🐱 Турецкая ангора",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnzKsYgQCvw2AQAyp85RCcp6UoEArg68i2QO7nWZjHaQ&s=10",
        "text": "Грациозная и лёгкая кошка с длинной шерстью.Характер: активная, умная, любит внимание и игры."
    },
    "ragdoll": {
        "name": "🐱 Рэгдолл",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDheyiDndiFQDHFLigsv3f1ZoZYuZiQNJmtFBIlpKRLrTf9lGPxwlceSg&s=10",
        "text": "Крупная, голубоглазая кошка с мягкой шерстью.Характер: очень спокойная, расслабляется на руках, как “тряпичная кукла”."
    },
    "sibir": {
        "name": "🐱 Сибирская кошка",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDspCPCpZoTjDxZ5a16hfnDSaJPa_6dfo-Hdx-vFIIX20rCDajitlohtJn&s=10",
        "text": "Пушистая, сильная и выносливая.Характер: умная, преданная, активная и смелая."
    },
    "siam": {
        "name": "🐱 Сиамская кошка",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0ZUBuskE19DJ31pZbYaHpsxvypW2fbBUDvqOQdJip5w&s=10",
        "text": "Стройная, с яркими голубыми глазами.Характер: очень разговорчивая, активная и общительная."
    },
    "bengal": {
        "name": "🐱 Бенгальская кошка",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfRvIFxj4Uq4kdyeE-8MhO_as_-H-nvr63itkzloRCcw&s=10",
        "text": "Похожа на мини-леопарда.Характер: энергичная, игривая, очень активная и умная."
    },
    "russian": {
        "name": "🐱 Русская голубая кошка",
        "photo": "https://storage.yandexcloud.net/yac-wh-sb-prod-s3-media-03002/uploads/article/files/cda5ba4216bfd820531772ae7916bc00.webp",
        "text": "Серебристо-голубая шерсть и зелёные глаза.Характер: тихая, аккуратная, немного застенчивая."
    },
    "shotland": {
        "name": "🐱 Шотландская вислоухая кошка",
        "photo": "https://www.purina.ru/sites/default/files/styles/ttt_image_510/public/2021-02/CAT%20BREED%20Hero%20Mobile_0010_Scottish_fold.jpg?itok=hLQmpCIR",
        "text": "Ушки сложены вперёд, милый внешний вид.Характер: спокойная, ласковая, домашняя."
    },
    "american": {
        "name": "🐱 Американская короткошёрстная кошка",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdYV7w5yND5AfdmKNqzzkQbqVw_ZwlFK7cHC2z09jj_JpjFBMyRj2l-I8Z&s=10",
        "text": "Крепкая и здоровая порода.Характер: дружелюбная, уравновешенная, легко адаптируется."
    },
    "don": {
        "name": "🐱 Донской сфинкс",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsT3C1tvSlF9zcYgycW9KeB4Gs1Q_V0fR_XS8ptOAOh9PmhpiAC-jDf5Xs&s=10",
        "text": "Мягкая кожа, иногда с лёгким пушком.Характер: добрый, общительный, сильно привязан к человеку."
    },
    "peter": {
        "name": "🐱 Петерболд",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgMsNOaqcq-Uoh3c23NtXkNsFCwcgRQUE7jpoWOQKsOQ&s=10",
        "text": "Изящная и стройная кошка.Характер: умная, активная, контактная."
    },
    "bambino": {
        "name": "🐱 Бамбино",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlBY2lzD5bzCvQzH0Ff-F_Bu_0k2POiQzV3HGIbXR2dg&s=10",
        "text": "Маленькая бесшёрстная кошка с короткими лапками.Характер: игривая, ласковая, очень домашняя."
    },
    "elf": {
        "name": "🐱 Эльф",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQF7s9uX7wX9wGXsL137eNB0xaZ9FXpmy7IMB7UmHmpYX1L_JHhHM90yhY&s=10",
        "text": "Редкая порода с загнутыми ушами.Характер: общительная, дружелюбная, необычная внешне."
    },
    "ukraine": {
        "name": "🐱 Украинский левкой",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcNLqcN7jSbhhmUHNhva6IfuqUnI_0q6ueUsl-XJfyFmIw7yyuvQI-Ffrl&s=10",
        "text": "Характер: спокойный, ласковый, привязан к хозяину."
    },
    "british": {
        "name": "🐱 Британец",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScKtlOrmAo8p_oQQCmxRHZ2UYDUXy0Bvak6w&s",
        "text": "Британская кошка — плюшевая, спокойная и независимая."
    },
    "sphynx": {
        "name": "🐱 Сфинкс",
        "photo": "https://yac-wh-sb-prod-s3-media-07001.storage.yandexcloud.net/media/images/sphinx.max-2880x1820.format-jpeg_SPtfFVj.jpg",
        "text": "Сфинкс — без шерсти, очень общительный и тёплый."
    }
}


# =======================
# 🧠 ТИПЫ → ПОРОДЫ
# =======================
def get_breeds(cat_type):
    data = {
        "long": [
            ("Мейн-кун", "mainecoon"),
            ("Персидская кошка", "persid"),
            ("Норвежская лесная кошка", "norweg"),
            ("Турецкая ангора", "turkey"),
            ("Рэгдолл", "ragdoll"),
            ("Сибирская кошка", "sibir"),
        ],
        "short": [
            ("Британец", "british"),
            ("Сиамская кошка", "siam"),
            ("Бенгальская кошка", "bengal"),
            ("Русская голубая кошка", "russian"),
            ("Шотландская вислоухая кошка", "shotland"),
            ("Американская короткошёрстная кошка", "american"),
        ],
        "hairless": [
            ("Сфинкс", "sphynx"),
            ("Донской сфинкс", "don"),
            ("Петерболд", "peter"),
            ("Бамбино", "bambino"),
            ("Эльф", "elf"),
            ("Украинский левкой", "ukraine"),
        ]
    }
    return data.get(cat_type, [])


# =======================
# 🚀 /START
# =======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🐱 Длинношёрстные", callback_data="long")],
        [InlineKeyboardButton("🐱 Короткошёрстные", callback_data="short")],
        [InlineKeyboardButton("🐱 Бесшёрстные", callback_data="hairless")]
    ]

    await update.message.reply_text(
        "Выбери тип кошек:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =======================
# 🔘 КНОПКИ
# =======================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    # =========================
    # 1. ВЫБОР ТИПА
    # =========================
    breeds = get_breeds(data)

    if breeds:
        context.user_data["current_type"] = data  # 🔥 сохраняем тип

        keyboard = [
            [InlineKeyboardButton(name, callback_data=code)]
            for name, code in breeds
        ]

        keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data="back")])

        await query.edit_message_text(
            "Выбери породу:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # =========================
    # 2. НАЗАД
    # =========================
    if data == "back":
        last_type = context.user_data.get("current_type")

        if not last_type:
            keyboard = [
                [InlineKeyboardButton("🐱 Длинношёрстные", callback_data="long")],
                [InlineKeyboardButton("🐱 Короткошёрстные", callback_data="short")],
                [InlineKeyboardButton("🐱 Бесшёрстные", callback_data="hairless")]
            ]

            await query.edit_message_text(
                "Выбери тип кошек:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return

        breeds = get_breeds(last_type)

        keyboard = [
            [InlineKeyboardButton(name, callback_data=code)]
            for name, code in breeds
        ]

        keyboard.append([InlineKeyboardButton("⬅️ Назад", callback_data="main")])

        # ⚠️ ВАЖНО: НЕ edit_message_text после media
        try:
            await query.edit_message_text(
                "Выбери породу:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        except:
            await query.message.delete()

            await query.message.reply_text(
                "Выбери породу:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        return
    # =========================
    # 3. ГЛАВНОЕ МЕНЮ
    # =========================
    if data == "main":
        keyboard = [
            [InlineKeyboardButton("🐱 Длинношёрстные", callback_data="long")],
            [InlineKeyboardButton("🐱 Короткошёрстные", callback_data="short")],
            [InlineKeyboardButton("🐱 Бесшёрстные", callback_data="hairless")]
        ]

        await query.edit_message_text(
            "Выбери тип кошек:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # =========================
    # 4. ПОРОДА (ФОТО)
    # =========================
    cat = cats.get(data)

    if cat:
        keyboard = [
            [InlineKeyboardButton("⬅️ Назад", callback_data="back")]
        ]

        await query.edit_message_media(
            media=InputMediaPhoto(
                media=cat["photo"],
                caption=f"{cat['name']}\n\n{cat['text']}"
            ),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return
# =======================
# 🆘 HELP
# =======================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start — открыть меню\n"
        "/help — помощь"
    )


# =======================
# ▶️ ЗАПУСК
# =======================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button))

    print("Бот запущен")
    app.run_polling()


if __name__ == "__main__":
    main()