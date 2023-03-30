# pylint: disable=invalid-name
import ast

from loguru import logger


class UnusedImportChecker(ast.NodeVisitor):
    def __init__(self):
        self.violations = []
        self.imports = set()
        self.names = set()

    def check(self, source_code) -> int:
        tree = ast.parse(source_code)
        self.visit(tree)
        return self.report()

    def report(self) -> int:
        result = 0
        for name, line in self.imports:
            if name not in self.names:
                result = 1
                logger.warning(f':{line}: unused import \'{name}\'')
        return result

    def visit_Import(self, node):
        self.add_imports(node)

    def visit_ImportFrom(self, node):
        self.add_imports(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.names.add(node.id)

    def add_imports(self, node):
        for import_name in node.names:
            name = import_name.name.partition(".")[0]
            self.imports.add((name, node.lineno))
