from dotenv import load_dotenv
import os

load_dotenv()

TEAMS_CLIENT_ID = os.getenv("TEAMS_CLIENT_ID")
TEAMS_CLIENT_SECRET = os.getenv("TEAMS_CLIENT_SECRET")
