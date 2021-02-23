from utils import get_environment_variable

POSTGRES_URI = get_environment_variable('POSTGRES_URI')
POSTGRES_DB = get_environment_variable('POSTGRES_DB')
POSTGRES_USERNAME = get_environment_variable('POSTGRES_USERNAME')
POSTGRES_PASSWORD = get_environment_variable('POSTGRES_PASSWORD')


class Config(object):
    uri_template = 'postgresql://{user}:{password}@{url}/{db}'

    SQLALCHEMY_DATABASE_URI = uri_template.format(
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        url=POSTGRES_URI,
        db=POSTGRES_DB
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


def get_config(env=None):
    if env is None:
        try:
            env = get_environment_variable('ENV')
        except Exception:
            env = 'development'
            print('env is not set, using env:', env)

    return DevelopmentConfig()
