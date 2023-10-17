import click

from .my_wordclouds import create_wordcloud


@click.command()
@click.version_option()
@click.option(
    "-i",
    "--inputfile",
    required=True,
    type=str,
    help="The input-file with text.",
)
def cli(inputfile: str) -> None:
    """Extract data from the database [NOT IMPLEMENTED YET].

    This command is not implemented yet.
    """
    try:
        create_wordcloud(inputfile)
    except click.ClickException as e:
        e.show()
        ctx = click.get_current_context()
        ctx.exit(e.exit_code)
