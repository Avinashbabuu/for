from os import environ 

class Config:
    API_ID = environ.get("API_ID", "21538384")
    API_HASH = environ.get("API_HASH", "9b8e9b10a5c34b67054aceca02bf423e")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8016050256:AAHytNlr1i0ovsbsSs-Myp30v2UA3bHrosg") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://avinashop62:avinashop62@cluster0.5y3t1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6484788124').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
