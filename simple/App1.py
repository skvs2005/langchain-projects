import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

GROQ_API_KEY=os.environ['GROQ_API_KEY']