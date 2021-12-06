import os
import sys

if __name__ == '__main__':
    # print("Updating the base path")
    root_path = os.path.abspath(os.path.join(os.getcwd(), '.'))
    sys.path.append(root_path)
    # print("Added module root:", root_path)

import click

from geoparser.cli.commands.indices import indices
from geoparser.cli.commands.landsat import landsat

@click.group()
def cli():
    pass

@click.command()
def about():
    click.echo('Hello from Geo Parser')

cli.add_command(about)
cli.add_command(indices)
cli.add_command(landsat)

if __name__ == '__main__':
    cli()