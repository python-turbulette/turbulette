# Settings needed by turbulette
SETTINGS_RULES = "SETTINGS_RULES"
SETTINGS_LOGS = "CONFIGURE_LOGGING"
SETTINGS_INSTALLED_APPS = "INSTALLED_APPS"
SETTINGS_DATABASE_SETTINGS = "DATABASE_SETTINGS"
SETTINGS_DATABASE_CONNECTION = "DATABASE_CONNECTION"
SETTINGS_DB_DSN = "DB_DSN"

# Special settings needed by turbulette
# see `simple_settings` documentation :
# https://github.com/drgarcia1986/simple-settings#special-settings
REQUIRED_SETTINGS = "REQUIRED_SETTINGS"
REQUIRED_SETTINGS_TYPES = "REQUIRED_SETTINGS_TYPES"
REQUIRED_NOT_NONE_SETTINGS = "REQUIRED_NOT_NONE_SETTINGS"


# Env variables
ENV_TURBULETTE_SETTINGS = "TURBULETTE_SETTINGS"

# Files and folders
FILE_ALEMBIC_INI = "alembic.ini"
FOLDER_ALEMBIC = "alembic"


# Apps that must always be loaded with turbulette
TURBULETTE_CORE_APPS = [
    "turbulette.apps.base"
]


# pytest settings
PYTEST_TURBULETTE_SETTINGS = "PYTEST_TURBULETTE_SETTINGS"
