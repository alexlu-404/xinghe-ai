import os
from pathlib import Path
import psycopg2
from dotenv import load_dotenv

# .env 在项目根目录；db.py 在 src/ 下，所以往上两级
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

def get_connection():
    """返回一个新的数据库连接。调用方负责关闭。"""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=os.getenv("DB_PORT", "5432"),
        client_encoding=os.getenv("DB_CLIENT_ENCODING", "utf8")
    )