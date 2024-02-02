from telegram.ext import *
import keys

print('starting up bot')

def start_command(update, context):
    update.message.reply_text('hi how are ya')

def start_command(update, context):
    update.message.reply_text('idlk')

def start_command(update, context):
    update.message.reply_text('hi how are ya')

def handle_responce(text:str) -> str:
    if 'hello' in text:
        return 'why are you even asking me '
    if 'bye' in text:
        return 'dont come back'
    return 'idk'


def handle_message(update, context):
    message_type = update.messege.chat.type
    text = str(update.message.text).lower()
    response=''

    print(f'user({Update.message.chat.id})says:"{text}in:{message_type}"')

    if message_type == 'group':
        if'@ghastmovies453_bot' in text:
            new_text = text.replace('@ghastmovies453_bot','').strip()
            response = handle_responce(new_text)
    else:
         response=handle_responce(text)
    update.message.reply_text(response)

def error(update,contex):
    print(f'update{update} caused error:{context.error}')

    if __name__ =='__main__':
        Updater =Updater(keys.token,use_context=True)
        dp= Updater.dispatcher
        #commands
        dp.add_handler(CommandHandler('start',start_command))
        dp.add_handler(CommandHandler('help',help_command))
        dp.add_handler(CommandHandler('custom',custom_command))

        dp.add_handler(MessageHandler(filters.text, handle_message))

        dp.add_error_handler(error)


        Updater.start_pulling(1.0)
        Updater.idle()