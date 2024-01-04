import os
from dotenv import load_dotenv

load_dotenv()

database = os.getenv("DATABASE")
user = os.getenv("USER")
host = os.getenv("HOST")
port = os.getenv("PORT")
password = os.getenv("PASSWORD")