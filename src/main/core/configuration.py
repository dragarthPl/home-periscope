import os
from pathlib import Path

from pydantic import BaseSettings
import yaml

yaml_configuration = dict()

root_path = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent.parent
with open(os.path.join(root_path, "config","configuration.yaml")) as f:
    yaml_configuration.update(yaml.load(f, Loader=yaml.FullLoader))


class Features:
    log_to_file: bool = yaml_configuration.get('features', {}).get('log_to_file', False)


class Configuration(BaseSettings):
    stream_ip: str = yaml_configuration['stream_ip']
    stream_port: int = yaml_configuration['stream_port']

    default_maximum_temperature: int = yaml_configuration['default_maximum_temperature']
    default_minimum_temperature: int = yaml_configuration['default_minimum_temperature']

    features = Features()
