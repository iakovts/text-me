import pathlib
import yaml

from typing import Any

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / "configs" / "text_me.yaml"


def get_config(path: pathlib.Path) -> dict[str, Any]:
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


config = get_config(config_path)
