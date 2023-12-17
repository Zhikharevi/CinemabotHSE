from logging.config import dictConfig
from pathlib import Path
from typing import Final

from yaml import full_load as yaml_load


CONFIG_FILE: Final[Path] = Path("logging.yml")


def setup_logger() -> None:
    config = yaml_load(CONFIG_FILE.read_bytes())
    dictConfig(config)
