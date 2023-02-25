# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "23223511"))
    API_HASH = os.environ.get("API_HASH", "c2207a11155ad050097e981fdd5fd0b1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5922782407:AAFi6d9x-rMnJb9WhlcNkeFm0jFMg8s1Alc")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 5630338878))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://samar:samar@ac-sjxwrus-shard-00-00.ayer8ux.mongodb.net:27017,ac-sjxwrus-shard-00-01.ayer8ux.mongodb.net:27017,ac-sjxwrus-shard-00-02.ayer8ux.mongodb.net:27017/?ssl=true&replicaSet=atlas-ghv0w6-shard-0&authSource=admin&retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001728595474"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
