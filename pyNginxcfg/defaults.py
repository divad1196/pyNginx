import os
from pathlib import Path

ROOT_PATH = Path(os.path.dirname(os.path.realpath(__file__))).resolve()
TEMPLATES_FOLDER = ROOT_PATH.joinpath("templates/").resolve()