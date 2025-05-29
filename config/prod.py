from .base import Settings

class ProdSettings(Settings):
    class Config:
        env_file = ".env.prod"
