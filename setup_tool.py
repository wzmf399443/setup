import click 
import sys
import os
__dirname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, __dirname + './python_tool')
from package_pyenv import *

@click.command()
@click.option("--install", nargs=1, required=False)
def main(install):
    click.echo("hi install")
    if install in 'pyenv':
        click.echo("Install :" +install)


# @click.group()
# def cli():
#     pass

# @cli.command()
# def initdb():
#     click.echo('Initialized the database')

# @cli.command()
# def dropdb():
#     click.echo('Dropped the database')

if __name__ == "__main__":
    main()