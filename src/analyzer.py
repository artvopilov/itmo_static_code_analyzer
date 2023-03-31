# pylint: disable=invalid-name


import ast
from typing import Set

from loguru import logger


class Analyzer(ast.NodeVisitor):
    _imports: Set[str]
    _names: Set[str]

    def check(self, source_code) -> int:
        self._reset()
        tree = ast.parse(source_code)
        self.visit(tree)
        return self._report()

    def _reset(self) -> None:
        self.violations = []
        self.imports = set()
        self.names = set()

    def _report(self) -> int:
        result = 0
        for name, line in self.imports:
            print(name, line)
            print(self.names)
            if name not in self.names:
                result = 1
                logger.warning(f':{line}: unused import \'{name}\'')
        return result

    def visit_Import(self, node):
        self._add_imports(node)

    def visit_ImportFrom(self, node):
        self._add_imports(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.names.add(node.id)

    def _add_imports(self, node):
        for import_name in node.names:
            name = import_name.name.partition(".")[0]
            self.imports.add((name, node.lineno))
