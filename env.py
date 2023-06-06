from dotenv import load_dotenv
import os

load_dotenv()

database = {
    'connection_string': os.getenv('DB_CONNECTION_STRING'), 
}
