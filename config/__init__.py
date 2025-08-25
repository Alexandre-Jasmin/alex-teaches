from config.development import DevelopmentConfig
from config.production import ProductionConfig
from config.testing import TestingConfig

def get_config(env):
    if env == "production":
        return ProductionConfig
    elif env == "testing":
        return TestingConfig
    return DevelopmentConfig
