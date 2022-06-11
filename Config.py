import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get("API_ID", "15663735"))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get("API_HASH", " 41ffd2a4ee5614e9a9269bdb818dcda3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5015892079:AAFa2B4p7lGv7isApfpzpb0hnsRz9LAE7CE")
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql") 
    MUST_JOIN = os.environ.get("MUST_JOIN", " HeroOfficialBots")
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    API_ID = 15663735
    API_HASH = "41ffd2a4ee5614e9a9269bdb818dcda3"
    BOT_TOKEN = "5015892079:AAFa2B4p7lGv7isApfpzpb0hnsRz9LAE7CE"
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "HeroOfficialBots"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
