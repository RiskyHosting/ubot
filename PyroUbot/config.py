import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7851958065").split()))

API_ID = int(os.getenv("API_ID", "36320479"))

API_HASH = os.getenv("API_HASH", "d7eb20a7a335d13dfba7cc5b7720bea5")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7999962174:AAFmnloJ4Ol_JVpH2dYM_2BvpY_Tue6vKhU")

OWNER_ID = int(os.getenv("OWNER_ID", "7851958065"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-5228925824").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Indiaindiahottt:Indiaindiahottt@indiaindiahottt.o3ihegl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-5012203930"))
