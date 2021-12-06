import click

from geoparser.services.landsat.LandsatDataUtils import LandsatDataUtils

@click.group()
def indices():
    pass

@click.command()
@click.argument('file-name')
def extract_ndvi(file_name):
    ldu = LandsatDataUtils()
    ldu.calculate_ndvi(file_name)


indices.add_command(extract_ndvi)
