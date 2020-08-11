from jinja2 import Environment, FileSystemLoader
from .defaults import TEMPLATES_FOLDER

LOADER = FileSystemLoader(
    str(TEMPLATES_FOLDER)
)

env = Environment(loader=LOADER)

def get_template(name):
    return env.get_template(name)

# def render(name, data, output: None):
#     template = get_template(name)
#     template.render