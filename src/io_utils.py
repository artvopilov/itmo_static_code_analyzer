# pylint: disable=unspecified-encoding
# pylint: disable=too-few-public-methods


class IOUtils:
    @staticmethod
    def read_file(path) -> str:
        with open(path) as file:
            return file.read()
