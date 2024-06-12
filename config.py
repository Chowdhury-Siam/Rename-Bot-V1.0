import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11721551")

API_HASH = os.environ.get("API_HASH", "9a19f18dfe587666c928ffa1479d2d9c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7366003305:AAH50pdBo-hlNyJ-UdrbG_fl7o1XY-Yohqc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Anime_Kun_Channel") 

DB_NAME = os.environ.get("DB_NAME","siam6338")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://ssiam4298:OlFHVeB7HYsw1523@siam60.pvnm15w.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/587e78b1375927d0cd3b8.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5971676967').split()]

PORT = os.environ.get("PORT", "8080")
