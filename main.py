import pyshorteners, telegram, re


def short(text):
    s = pyshorteners.Shortener(domain='https://ttm.sh')
    shorted = s.nullpointer.short(text)

    return (shorted)

def link(text):
    regex = r'('
    regex += r'(?:(https?|s?ftp):\/\/)?'
    regex += r'(?:www\.)?'
    regex += r'('
    regex += r'(?:(?:[A-Z0-9][A-Z0-9-]{0,61}[A-Z0-9]\.)+)'
    regex += r'([A-Z]{2,6})'
    regex += r'|(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    regex += r')'
    regex += r'(?::(\d{1,5}))?'
    regex += r'(?:(\/\S+)*)'
    regex += r')'
    linkex = re.compile(regex, re.IGNORECASE)
    url = linkex.search(text)
    x = url.group(0).strip()
    return x



TelegramBot = "5236892500:AAHRvy4GdRWq3Cr0Ccy3c58TjNsEx_hxLn4"

def webhook(request):
    bot = telegram.Bot(token=TelegramBot)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        text = str(update.message.text)
        ChatID = update.message.chat_id
        try:
            link = text
            shorted = short(link)
            bot.send_message(chat_id=ChatID, text=shorted)

        except:
            update.message.reply_text("I'm sorry, I couldn't help you this time.\nplease try again later.")
    return "ok"

