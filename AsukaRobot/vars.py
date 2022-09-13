from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:

    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-1001747095795))

class Development:

    MESSAGE_DUMP = -1001747095795
