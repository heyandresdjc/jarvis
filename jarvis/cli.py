import click


@click.group()
def cli():
    pass


@click.command()
def initdb():
    print('Initialized the database')


@click.command()
def dropdb():
    print('Dropped the database')


cli.add_command(initdb)
cli.add_command(dropdb)
