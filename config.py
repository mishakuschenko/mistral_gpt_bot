from dotenv import load_dotenv
from os import getenv

load_dotenv()

ai_token = getenv('AI_TOKEN')
token= getenv('TOKEN') 

models = {
    "mistral-large-latest": "mistral-large-latest", 
    "pixtral-large-latest": "pixtral-large-latest",
    "ministral-3b-latest": "ministral-3b-latest",
    "ministral-8b-latest": "ministral-8b-latest",
} 

