from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def country_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🇹🇷 Turkey", callback_data="turkey"),
            InlineKeyboardButton("🇰🇿 Kazakhstan", callback_data="kazakhstan"),
        ],
        [
            InlineKeyboardButton("🇷🇺 Russia", callback_data="russia"),
            InlineKeyboardButton("🇵🇱 Poland", callback_data="poland"),
        ],
        [
            InlineKeyboardButton("🇹🇯 Tajikistan", callback_data="tajikistan"),
            InlineKeyboardButton("🇰🇬 Kyrgyzstan", callback_data="kyrgyzstan"),
        ],
        [
            InlineKeyboardButton("🇹🇲 Turkmenistan", callback_data="turkmenistan"),
            InlineKeyboardButton("🇺🇿 Uzbekistan", callback_data="uzbekistan"),
        ],
        [
            InlineKeyboardButton("🌍 Other Countries", callback_data="other")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
