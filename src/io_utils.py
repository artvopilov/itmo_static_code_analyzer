class IOUtils:
    @staticmethod
    def read_file(path) -> str:
        with open(path) as file:
            return file.read()
