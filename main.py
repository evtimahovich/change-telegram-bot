"""Telegram Bot для CHANGE Recruitment Center""" 
import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class ChangeBot:
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.sheets_id = os.getenv('GOOGLE_SHEETS_ID')
        self.admin_ids = list(map(int, os.getenv('ADMIN_TELEGRAM_IDS', '').split(',')))
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_user.id not in self.admin_ids:
            await update.message.reply_text("❌ У вас нет доступа")
            return
        keyboard = [['📊 Статус', '📈 Аналитика'], ['📋 Последние договоры']]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text('🤖 CHANGE Recruitment Bot запущен!', reply_markup=reply_markup)
    
    def run(self):
        app = Application.builder().token(self.bot_token).build()
        app.add_handler(CommandHandler('start', self.start))
        logger.info('🚀 Bot starting...')
        app.run_polling()

if __name__ == '__main__':
    bot = ChangeBot()
    bot.run()
