from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    acces_token_expire_minutes:int

    class Config:
        env_file = '.env'

settings = Settings(database_hostname='kavfu5f7pido12mr.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                    database_port='3306',
                    database_password='ldxj2fozcxpw2nzg',
                    database_name='cdn1ak0olosxovnd',
                    database_username='c0qo6o6vfhk0pl9x')