# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 18233797))
    API_HASH = os.environ.get("API_HASH", "6cad012cd66ba62e1b7d49f1f84742d1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5323640419:AAFXnGnqWvZhuUtZUrPU9AX06aX_WPwbF4M")
    DOWNLOAD_LOCATION = "./Downloads"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 5195985707))
    LOG_CHANNEL = int(os.environ.get(-1001667535152))
    UPDATES_CHANNEL = os.environ.get("megadllog", None)


class TEXT:
  ABOUT = """
🤖 **Nombre:** {bot_name}

📝 **Lenguaje:** [Python](https://www.python.org)

📚 **Librería:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosteado en:** [Heroku](https://heroku.com)

🧑‍💻 **Desarrollador:** [yordante](https://t.me/yordante)

👥 **Grupo de soporte:** [Full Series Cloud](https://t.me/Full_Series_Cloud)

📢 **Canal de actualizaciones:** [Full Series Cloud](https://t.me/Full_Series_Cloud)
"""

  HELP_USER = """
This is **{bot_name}**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 

**Made With ❤️ By @AsmSafone! 👑**
"""

  START_TEXT = """
👋🏻 **Hola** {user_mention},

Soy **{bot_name}**
Puedo descargar archivos y ideos de enlaces de MEGA y subirlos a Telegram. Lea la ayuda para más información 😉!

**Creador: {bot_owner}**❤️!
"""
