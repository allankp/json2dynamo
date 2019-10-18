import click
from json2dynamo.util import JsonTransfromer


@click.command()
@click.argument("inputpath", type=click.Path(exists=True))
@click.argument("outputpath", type=click.Path())
def cli(inputpath, outputpath):
    JsonTransfromer().transform_json_files(inputpath, outputpath)
    click.echo(click.style(f"Transformation completed: {outputpath}", fg="green"))
