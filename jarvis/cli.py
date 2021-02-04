import os
import click


@click.group()
def cli():
    pass


@cli.command()
def install_brew():
    os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')


@cli.command()
def install_compose():
    os.system('sudo curl -L "https://github.com/docker/compose/releases/download/'
              '1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    os.system('sudo chmod +x /usr/local/bin/docker-compose')


@cli.command()
def install_awscli():
    os.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
    os.system('unzip awscliv2.zip')
    os.system('sudo ./aws/install')


cli.add_command(install_brew)
cli.add_command(install_awscli)
cli.add_command(install_compose)


if __name__ == '__main__':
    cli()
