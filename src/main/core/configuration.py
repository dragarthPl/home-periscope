import os
from pathlib import Path

from pydantic import BaseSettings
import yaml

yaml_configuration = dict()

root_path = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent.parent
with open(os.path.join(root_path, "config","configuration.yaml")) as f:
    yaml_configuration.update(yaml.load(f, Loader=yaml.FullLoader))


class Configuration(BaseSettings):
    stream_ip = yaml_configuration['stream_ip']
    stream_port = yaml_configuration['stream_port']
