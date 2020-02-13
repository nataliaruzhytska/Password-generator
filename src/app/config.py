import os


CHECK_PASS_API = 'https://api.pwnedpasswords.com/range/'


class Config:
    TEST_VALUE = "CONFIG_VALUE"
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    PG_USER = "pass_gen_admin"
    PG_PASSWORD = "simplepass"
    PG_HOST = "db"
    PG_PORT = 5432
    DB_NAME = "pass_gen_db"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class DevConfig(Config):
    TEST_VALUE = "DEV_CONFIG_VALUE"


class TestConfig(Config):
    TEST_VALUE = "TEST_CONFIG_VALUE"


def get_config(env):
    env = os.environ.get("ENV")
    dict_config = {"TEST": TestConfig,
                   "DEV": DevConfig,
                   "": Config
                   }
    return dict_config.get(env)
