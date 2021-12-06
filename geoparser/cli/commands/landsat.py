import click

from geoparser.services.landsat.LandsatDataUtils import LandsatDataUtils

@click.group()
def landsat():
    pass

@click.command()
@click.argument('file-name')
@click.argument('target')
def download_file(file_name, target):
    print('Downloading file {} to {}'.format(file_name, target))
    ldu = LandsatDataUtils()
    ldu.download_file(file_name, target)

@click.command()
@click.argument('dirname')
@click.argument('targetdir')
def extract_tiles(dirname, targetdir):
    ldu = LandsatDataUtils()
    ldu.extract_tiles(dirname, targetdir)


@click.command()
@click.argument('file-name')
def file_info(file_name):
    print('Loading details for ', file_name)
    ldu = LandsatDataUtils()
    ldu.download_file(file_name)


landsat.add_command(file_info)
landsat.add_command(extract_tiles)
landsat.add_command(download_file)