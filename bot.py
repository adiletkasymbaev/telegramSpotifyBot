import telebot
from sqlalchemy import and_, or_
from db_models import Song
from db_config import session

TOKEN = "8399648534:AAFvCsM552fBqmS0gyNZ5wQ2ckkOMmuGWGY"
bot = telebot.TeleBot(TOKEN)

def smart_search(query):
    words = query.split(" ")
    conditions = []

    for word in words:
        pattern = f"%{word}%"
        conditions.append(
            or_(
                Song.author.ilike(pattern),
                Song.name.ilike(pattern),
                Song.path.ilike(pattern),
            )
        )

    return session.query(Song).filter(
        and_(*conditions)
    ).all()

@bot.message_handler()
def any_handler(message):
    results = smart_search(message.text)

    if len(results) != 0:
        for song in results:
            with open(song.path, 'rb') as audio:
                bot.send_audio(
                    message.chat.id,
                    audio=audio,
                    title=song.name,
                    performer=song.author
                )
    else:
        bot.send_message(
            message.chat.id,
            "Песня не найдена!"
        )

bot.infinity_polling()