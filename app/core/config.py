import os

class Config:
    DEVZ_SECRET_KEY = os.getenv('DEVZ_SECRET_KEY')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    