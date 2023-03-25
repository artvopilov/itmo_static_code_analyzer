import click
import sys


from src.analyzer import UnusedImportChecker
from src.io_utils import IOUtils


@click.command()
@click.option('--source-file', '-s', required=True, type=str)
def main(source_file: str) -> None:
    source_code = IOUtils.read_file(source_file)

    analyzer = UnusedImportChecker()
    result = analyzer.check(source_code)
    sys.exit(result)


if __name__ == '__main__':
    main()
