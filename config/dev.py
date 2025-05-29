from .base import Settings

class DevSettings(Settings):
    class Config:
        env_file = ".env.dev"
