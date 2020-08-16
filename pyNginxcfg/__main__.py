import click
import odoorpc
import json
from .schemas import SiteEnableSchema
from .env import get_template
# from pathlib import Path

@click.command()
@click.argument("url", default="localhost")
@click.argument("user")
@click.option("--port", default=8069)
@click.option("--db")
@click.option(
    "--password",
    prompt=True,
    hide_input=True
)
@click.option(
    "--format",
    type=click.Choice([
        "json",
    ],
    case_sensitive=False),
    default="json",
)
def from_odoo_url(url, port, db, user, password, format="json"):
    odoo = odoorpc.ODOO(url, port=port)
    odoo.login(db, user, password)
    rep = odoo.http("server_inventory/nginx_config")
    content = rep.read().decode()
    rep.close()

    if format == "json":
        data = json.loads(content)

    enable_configs = SiteEnableSchema.validate(data)
    template = get_template("site.j2")
    for cfg in enable_configs:
        filename = cfg["server_name"]
        with open(filename, "w") as f:
            f.write(template.render(config=cfg))


from_odoo_url()