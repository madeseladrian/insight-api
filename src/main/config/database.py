from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_days: int
    storage_bucket: str

    class Config:
        env_file = '.env'

settings = Settings()
