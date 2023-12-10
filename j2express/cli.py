import click


@click.command()
def main():
    """Prints a greeting."""
    click.echo("Hello, World!")


if __name__ == '__main__':
    main()
