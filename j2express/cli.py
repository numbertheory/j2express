import click

@click.command()
@click.option('-f', '--filename', help='J2 Template to process')
def main(filename):
    click.echo("Hello, World!")
    click.echo(filename)


if __name__ == '__main__':
    main()
