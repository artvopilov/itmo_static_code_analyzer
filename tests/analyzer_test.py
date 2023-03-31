from src.analyzer import Analyzer


class TestAnalyzer:
    _ANALYZER = Analyzer()

    def test_1(self) -> None:
        source_code = 'import math\n\n' \
                      'a = 1\n' \
                      'b = 2\n' \
                      'c = math.sum(a, b)\n'
        result = self._ANALYZER.check(source_code)
        assert result == 0

    def test_2(self) -> None:
        source_code = 'import math\n' \
                      'a = 1\n' \
                      'b = 2\n' \
                      'c = a + b\n'
        result = self._ANALYZER.check(source_code)
        assert result != 0
