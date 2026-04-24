import os
from typing import Set


def _split_int_set(raw: str, fallback: str = "") -> Set[int]:
    source = (raw or fallback or "").strip()
    items = set()
    for part in source.split(','):
        part = part.strip()
        if not part:
            continue
        try:
            items.add(int(part))
        except ValueError:
            continue
    return items


def _env_bool(name: str, default: bool = False) -> bool:
    value = (os.environ.get(name, "") or "").strip().lower()
    if not value:
        return default
    return value in {"1", "true", "yes", "on"}


BOT_TOKEN = (os.environ.get("BOT_TOKEN", "") or "").strip()
ADMIN_ID = int(os.environ.get("ADMIN_ID", "7353041224"))
EXTRA_ADMIN_IDS = _split_int_set(os.environ.get("EXTRA_ADMIN_IDS", ""), "7353041224")
HELP_USERNAME = (os.environ.get("HELP_USERNAME", "@realupilootsupport") or "@realupilootsupport").strip()
MESSAGE_EFFECT_ID = (os.environ.get("MESSAGE_EFFECT_ID", "5104841245755180586") or "5104841245755180586").strip()
DEFAULT_FORCE_JOIN_CHANNELS = "@skullmodder,@botsarefather,@upilootpay"


def _split_channel_list(raw: str, fallback: str = ""):
    source = (raw or fallback or "").strip()
    channels = []
    for part in source.split(","):
        channel = part.strip()
        if not channel:
            continue
        # Telegram accepts either numeric chat IDs or @usernames for get_chat_member.
        if channel.lstrip("-").isdigit():
            try:
                channels.append(int(channel))
            except ValueError:
                channels.append(channel)
        else:
            channels.append(channel)
    return channels


FORCE_JOIN_CHANNELS = _split_channel_list(os.environ.get("FORCE_JOIN_CHANNELS", ""), DEFAULT_FORCE_JOIN_CHANNELS)
REQUEST_CHANNEL = (os.environ.get("REQUEST_CHANNEL", "https://t.me/+kOrz7X6VUygyYjk1") or "").strip()
NOTIFICATION_CHANNEL = (os.environ.get("NOTIFICATION_CHANNEL", "@upilootpay") or "").strip()
WELCOME_IMAGE = (os.environ.get("WELCOME_IMAGE", "https://image2url.com/r2/default/images/1775843670811-7e698bcc-a37c-46f9-a0bd-6a5cabe5f6ec.png") or "").strip()
WITHDRAWAL_IMAGE = (os.environ.get("WITHDRAWAL_IMAGE", "https://www.image2url.com/r2/default/images/1776788724967-d1a0d23e-7add-4b97-953e-23ddc3e70500.jpg") or "").strip()
BOT_USERNAME = (os.environ.get("BOT_USERNAME", "realupilootbot") or "realupilootbot").strip().lstrip('@')
DB_PATH = (os.environ.get("DB_PATH", "/data/bot_database.db") or "/data/bot_database.db").strip()
PUBLIC_BASE_URL = (os.environ.get("PUBLIC_BASE_URL", "") or "").strip()
SKIP_PENDING_UPDATES = _env_bool("SKIP_PENDING_UPDATES", True)
