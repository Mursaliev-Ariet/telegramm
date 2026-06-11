from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8649785856:AAH6EGjgrCEPiE2D25kEL1JPEX4NTAMMINY"

cats = {
    "mainecoon": {
        "name": "🐱 Мейн-кун",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRduiCiBFEmhy_CoVIlPP0deMRiDuWCl2vOZA&s",
        "text": "Мейн-кун — одна из самых крупных пород кошек. У них длинная пушистая шерсть, большие лапы и кисточки на ушах. Обычно спокойные, дружелюбные и любят общение."
    },

    "british": {
        "name": "🐱 Британец",
        "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScKtlOrmAo8p_oQQCmxRHZ2UYDUXy0Bvak6w&s",
        "text": "British Shorthair — кошка с густой плюшевой шерстью и круглой мордочкой. Часто спокойная, независимая и любит комфортный отдых рядом с хозяином."
    },

    "sphynx": {
        "name": "🐱 Сфинкс",
        "photo": "https://yac-wh-sb-prod-s3-media-07001.storage.yandexcloud.net/media/images/sphinx.max-2880x1820.format-jpeg_SPtfFVj.jpg",
        "text": "Sphynx cat — необычная порода почти без шерсти. Такие кошки обычно очень общительные, любят тепло и часто ищут внимание человека."
    }
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🐱 Мейн-кун", callback_data="mainecoon")],
        [InlineKeyboardButton("🐱 Британец", callback_data="british")],
        [InlineKeyboardButton("🐱 Сфинкс", callback_data="sphynx")]
    ]

    await update.message.reply_text(
        "Выбери породу кошки 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update, context):

    query = update.callback_query
    await query.answer()

    cat = cats[query.data]

    await query.message.reply_photo(
        photo=cat["photo"],
        caption=f"{cat['name']}\n\n{cat['text']}"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start — открыть список пород\n"
        "/help — помощь"
    )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(CallbackQueryHandler(button))

    print("Бот запущен")
    app.run_polling()


if __name__ == "__main__":
    main()