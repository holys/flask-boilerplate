import os


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


CONFIG_MAP = {
    "product": ProductionConfig,
    "develop": DevelopmentConfig,
    "testing": TestingConfig,
}

env = os.environ.get("APP_SETTINGS", "develop")
CONFIG = CONFIG_MAP[env]


def is_develop_env():
    return env == "develop"


def is_product_env():
    return env == "product"


def is_testing_env():
    return env == "testing"
