from typing import List

import click
import sys


from src.analyzer import Analyzer
from src.io_utils import IOUtils


@click.command()
@click.option('--source-files', '-s', required=True, multiple=True)
def main(source_files: List[str]) -> None:
    analyzer = Analyzer()
    exit_code = 0
    for source_file in source_files:
        source_code = IOUtils.read_file(source_file)
        result = analyzer.check(source_code)
        exit_code = max(exit_code, result)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
