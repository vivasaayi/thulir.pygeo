import click

from geoparser.services.landsat.LandsatDataUtils import LandsatDataUtils

@click.group()
def indices():
    pass

@click.command()
@click.argument('dirname')
@click.argument('targetdir')
def extract_ndvi(dirname, targetdir):
    ldu = LandsatDataUtils()
    ldu.calculate_ndvi(dirname, targetdir)


indices.add_command(extract_ndvi)
