from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER     : str = 'postgres'
    POSTGRES_PASSWORD : str = 'password'
    POSTGRES_IP       : str = 'localhost'
    POSTGRES_PORT     : str = '5432'
    POSTGRES_DB       : str = 'micro2_db'

settings = Settings()
