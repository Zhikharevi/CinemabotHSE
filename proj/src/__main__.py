from src.config import Config
from src.executor import executor
from src.factory import setup_factory
from src.utils.logger import setup_logger


def main() -> None:
    setup_logger()
    config = Config()
    factory = setup_factory(config=config)
    executor(factory=factory)


if __name__ == "__main__":
    main()
