from .base import Settings

class TestSettings(Settings):
    class Config:
        env_file = ".env.test"
