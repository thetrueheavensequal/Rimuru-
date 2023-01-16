"""
MIT License

Copyright (c) 2022 ABISHNOI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- KingAbishnoi ""

import json
import os


def get_user_list(config, key):
    with open("{}/Exon/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "21927988"
    API_HASH = "e18f720acdff1e5b0ec80616aecd8a5a"
    APP_ID = "21927988"  # 2nd API_ID
    APP_HASH = "e18f720acdff1e5b0ec80616aecd8a5a"  # 2ns API_HASH
    ARQ_API_KEY = "QOYIDT-TJPPDA-JVVIZH-BTHMBB-ARQ"
    BOT_ID = "5881951624"
    TOKEN = "5881951624:AAHLQF582RVuIYRSide3FGjPKi-WdzoSiaI"
    OWNER_ID = "2064735436"
    OPENWEATHERMAP_ID = "687af7aaae4f454314ca54bfd8cddceb"
    OWNER_USERNAME = "plumblossomsword"
    BOT_USERNAME = "RimuruX_Bot"
    SUPPORT_CHAT = "theoneandonlymurim"
    UPDATES_CHANNEL = "rimurubotsnetwork"
    SUPPORT_CHANNEL = "theoneandonlymurm"
    JOIN_LOGGER = "-1001859171071"
    EVENT_LOGS = "-1001859171071"
    ERROR_LOGS = "-1001859171071"

    SQLALCHEMY_DATABASE_URI = "postgresql://memulsis:ghfzuk0DXS2NW4RURhV5kLV3puo3Wa5F@snuffleupagus.db.elephantsql.com/memulsis"  # sql
    DATABASH_URL = "postgresql://memulsis:ghfzuk0DXS2NW4RURhV5kLV3puo3Wa5F@snuffleupagus.db.elephantsql.com/memulsis"  # sql
    DB_URL = "postgresql://memulsis:ghfzuk0DXS2NW4RURhV5kLV3puo3Wa5F@snuffleupagus.db.elephantsql.com/memulsis"
    MONGO_DB_URL = "mongodb+srv://plumblossomsword:9fl2pP1p2I72vbS2@cluster0.oytdvq8.mongodb.net/?retryWrites=true&w=majority"  # needed for any database modules
    MONGO_URL = "mongodb+srv://plumblossomsword:9fl2pP1p2I72vbS2@cluster0.oytdvq8.mongodb.net/?retryWrites=true&w=majority"
    DB_URL2 = "mongodb+srv://plumblossomsword:9fl2pP1p2I72vbS2@cluster0.oytdvq8.mongodb.net/?retryWrites=true&w=majority"  # YOUR MONGO_DB_URI
    ARQ_API_URL = "https://arq.hamker.in"
    BOT_API_URL = "https://api.telegram.org/bot"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "zKSTO8g_x3qmaMrU_tiTRXibTb532qbmTKXYW3RdyW8Pq0qk1oEtqddo7HqxRp~1"
    SPAMWATCH_SUPPORT_CHAT = "@SpamwatchSupport"

    REDIS_URL = "rediss://red-cf0rlmirrk05t6t5p3qg:RniRsIOnT6UPiAxVD2QcdaIkwRj7RUye@frankfurt-redis.render.com:6379"

    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "whitelists")
    DEMONS = get_user_list("elevated_users.json", "supports")
    INSPECTOR = get_user_list("elevated_users.json", "sudos")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = "https://t.me/plumblossomsword"
    CERT_PATH = None
    STRICT_GBAN = "True"
    PORT = "5000"
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 10
    BAN_STICKER = "CAACAgUAAx0CbtCy_wACBPljwrhdi9tBj1pUKc9kHu4WNjGo5gACtwgAAlIl0VT9IuTRAoPKPi0E"
    ALLOW_EXCL = True
    CASH_API_KEY = "6HZ09C7DZYKWBCCE"
    TIME_API_KEY = "4ID9HHBVU5L8"
    WALL_API = "6950f5ds6a3"
    AI_API_KEY = ""
    BL_CHATS = []
    SPAMMERS = None
    SPAMWATCH_API = "zKSTO8g_x3qmaMrU_tiTRXibTb532qbmTKXYW3RdyW8Pq0qk1oEtqddo7HqxRp~1"
    ALLOW_CHATS = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    REM_BG_API_KEY = "K2dsdsYma6cZx"
    LASTFM_API_KEY = "9d73c8bfc43204b8087a8d4cb8f6dcb6"
    CF_API_KEY = ""
    BL_CHATS = []
    MONGO_PORT = "27017"
    MONGO_DB = "EXON"
    PHOTO = "https://te.legra.ph/file/400154519025c2513f6a6.jpg"
    HELP_IMG = "https://telegra.ph/file/22bf4ee4be93ba31d7ecb.jpg"
    START_IMG = "https://te.legra.ph/file/20b6e74f7bc48a17d1e7f.jpg"
    TIME_API_KEY = "4ID9HHBVU5L8"
    INFOPIC = True
    GENIUS_API_TOKEN = "e-8UdRQNrIssPyM"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True


# ENJOY
